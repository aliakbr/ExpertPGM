from cx_Freeze import setup, Executable
import os

base = None


executables = [Executable("GUI_main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },

}

os.environ['TCL_LIBRARY'] = r'C:\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python35\tcl\tk8.6'

setup(
    name = "ExpertPGM",
    options = options,
    version = "1.0",
    description = 'Tugas AI Kelompok 21',
    executables = executables
)