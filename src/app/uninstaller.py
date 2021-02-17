#Openstore app. Uninstaller
#IMPORTANT FILE! READ CHANGES THROUGH CAREFULLY!

#Module importing
import shutil #For I/O
import sys #TO get the package
if len(sys.argv) == 1:
    print("Not enough args!")
    quit

shutil.rmtree("../apps/" + sys.argv[1] + "/")

if (sys.argv[1] in open("../apps/installed.lst").readlines()):
    packageWrite = open("../apps/installed.lst", "r+").readlines()
    packageWrite.remove(sys.argv[1])
    open("../apps/installed.lst", "w").writelines(packageWrite)