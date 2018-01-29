"""This module exports the AutoIt plugin class."""

from cuda_lint import Linter, util
import os


class AutoIt(Linter):
    """Provides an interface to Au3Check.exe."""

    cmd = 'Au3Check -q -I'
    syntax = 'AutoIt'
    tempfile_suffix = 'au3'

    # "D:\Test\File.au3"(38,5) : error: asda(): undefined function.

    regex = r'"(?P<match>.*)"\((?P<line>\d+),(?P<col>\d+)\)\s:\s(?P<type>.*?):\s(?P<message>.*)'
    error_stream = util.STREAM_STDOUT


    def split_match(self, match):
        """Return the components of the error."""
        split_match = super(AutoIt, self).split_match(match)
        match, line, col, error, warning, message, near = split_match
        message = '{} (Col {})'.format(message, col)

        if match and match.group('type') == 'error':
            error = 1
            message = 'Error: ' + message
        elif match and match.group('type') == 'warning':
            warning = 1
            message = 'Warning: ' + message

        return match, line, col, error, warning, message, ''


    def run(self, cmd, code):
        """Overwrite linter function for adding include dir parameter."""
        cmd.append(os.path.dirname(self.filename))
        return self.tmpfile(cmd, code, suffix=self.get_tempfile_suffix())
