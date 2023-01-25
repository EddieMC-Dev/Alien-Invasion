import cx_Freeze
import sys

base=None
if (sys.platform=="win32"):
    base="Win32GUI"
executables = [cx_Freeze.Executable('alien_invasion.py', base=base)]

cx_Freeze.setup(
    name="main",
    options={'build_exe': {'packages':['pygame'],}},

    executables = executables
    
)