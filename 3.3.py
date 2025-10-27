import os
import sys
import platform
import sysconfig
print("os name",os.name)
print(os.getcwd())
print(os.listdir())
print(os.getlogin())
print("platform name",sys.platform)
print("platform.system()",platform.system())
print("platform.release()",platform.release())
