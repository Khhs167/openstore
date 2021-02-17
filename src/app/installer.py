#Openstore app. Installer
#IMPORTANT FILE! READ CHANGES THROUGH CAREFULLY!

#Module importing
import sys #Need it for the args
import requests #For downloading
import json #For reading data
import os #For I/O

if len(sys.argv) == 1:
    print("Not enough args!")
    quit

package = sys.argv[1]

oldDir = os.getcwd()
print("Collecting data about " + package + "...")
url = "https://raw.githubusercontent.com/Khhs167/openstore/main/apps/" + package + "/package.json"
r = requests.get(url, allow_redirects=True)
if not os.path.isdir("../temp/"):
    os.mkdir("../temp/")
open('../temp/package.json', 'w+').write(r.content)
packageInfo = json.load(open('../temp/package.json'))
if not os.path.isdir("../apps/"):
    os.mkdir("../apps/")
if not os.path.isdir("../apps/" + package):
    os.mkdir("../apps/" + package)
print("Downloading package...")
for dep in packageInfo["deps"]:
    url = "https://raw.githubusercontent.com/Khhs167/openstore/main/apps/" + package + "/" + dep["path"]
    r = requests.get(url, allow_redirects=True)
    open("../apps/" + package + "/" + dep["path"], 'w+').write(r.content)
os.chdir("../apps/" + package + "/")
os.system("chmod +x " + packageInfo["installScript"])
os.system("./" + packageInfo["installScript"])
os.chdir(oldDir)
os.remove("../temp/package.json")
if not (package in open("../apps/installed.lst").readlines()):
    packageWrite = open("../apps/installed.lst", "r+").readlines()
    packageWrite.append(package)
    open("../apps/installed.lst", "w+").writelines(packageWrite)