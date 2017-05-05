Linter for CudaLint plugin.
It adds support for AutoIt lexer.
It uses "Au3Check.exe -q".

If Au3Check.exe is not in PATH change the line
cmd = 'Au3Check -q'
in linter.py to the correct path.

Or create file "Au3Check.cmd" in any dir of PATH which contains the correct path:

"P:/Portable/AutoIt3/Au3Check.exe" %1 %2 %3 %4 %5 %6 %7 %8 %9

Author: Tom Braider