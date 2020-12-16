from cx_Freeze import *

includefiles = ['cal.ico']
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", #Shortcut
    "DesktopFolder", #Directory
    "My Calculator", #None
    "TARGETDIR", #Component
    "[TARGETDIR]\simplecalculator.exe",
    None,# Arguments
    None,#Descriptiion
    None,#Hotkey
    None,#Icon
    None,#IconIndex
    None,#ShowCmd
    "TARGETDIR", #wkDir

    )

]    
msi_data = {"Shortcut":shortcut_table}

#Change some default MSI option and specify the use of the above define table

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "My Calculator",
    author = "Saurabh Mohite",
    name ="My Simple Calculator",
    options = {'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options, },
    executables=[
        Executable(
            script="simplecalculator.py",
            base=base,
            icon='cal.ico',
        )
    ]
)