from http.server import executable
import sys
from cx_Freeze import setup, Executable

includes = []
include_files = ['themes']

print(sys.platform)

base="Win32GUI" if sys.platform=="win32" else None

setup(
    name="Library", 
    version="0.1", 
    description="Library management system",
    options={"build_exe": {"includes": includes, "include_files": include_files}},
    executables=[Executable("index.py", base=base)]
    )