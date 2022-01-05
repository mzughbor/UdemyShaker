import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # Code of your program here
    try:
        m = os.getcwd()
        command = 'SETX PATH "%path%;' + str(m) + '"'
        print(command)
        os.system(command)
        # m + '\\shaka-packager.exe'
    except Exception as e:
        print(e)

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# C:\Users\hp\PycharmProjects\UdemyDownloader\venv\Scripts