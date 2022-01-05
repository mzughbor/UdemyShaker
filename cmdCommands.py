
import os
try:
    m = os.getcwd()
    command = 'SETX PATH "%path%;' + str(m)
    print(command)
    os.system(command)
    # m + '\\shaka-packager.exe'
except Exception as e:
    print(e)