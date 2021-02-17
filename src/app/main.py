#Openstore app. GUI handler
#IMPORTANT FILE! READ CHANGES THROUGH CAREFULLY!

#TODO
#Add simple GUI
#Add downloading


#Module importing
import tkinter as tk #Importing tkinter in order to create GUI. Calling it tk because it is easy to remember and short
from tkinter import messagebox #Import messagebox, so that we can display info
import os #For info
import requests #To get package list
from inspect import stack
import functools

#Function Defintion
def ShowInfo():
    '''Shows the application information located in /data/application.txt'''
    messagebox.showinfo(title="Information", message=open("data/application.txt", "r").read())

def Install(app):
    '''Shows the application information located in /data/application.txt'''
    os.system("python installer.py " + app)

def UnInstall(app):
    apps.destroy()
    '''Shows the application information located in /data/application.txt'''
    os.system("python uninstaller.py " + app)
    BrowseRemove()
def BrowseInstall():
    global apps
    global root
    root.withdraw()
    apps = tk.Tk()
    apps.title("OpenStore")
    tk.Label(apps, text="App browser").pack()
    print("Fetching lists")
    url = "https://raw.githubusercontent.com/Khhs167/openstore/main/apps/apps.lst"
    r = requests.get(url, allow_redirects=True)
    installed = open("../apps/installed.lst").readlines()
    boxes = {}
    for app in r.content.decode('utf-8').split("\n")[:len(r.content.decode('utf-8').split("\n"))-1]:
        newBox = InstallButton(apps, text=app)
        newBox.app = str(app)
        eval("newBox.config(command=functools.partial(Install,\"" + app + "\"))")
        newBox.pack()
    apps.geometry("200x500")
    print("Browsing stopped")
    root.deiconify() 

def BrowseRemove():
    global apps
    global root
    root.withdraw()
    apps = tk.Tk()
    apps.title("OpenStore")
    tk.Label(apps, text="App browser").pack()
    print("Fetching lists")
    r = open("../apps/installed.lst").readlines()
    boxes = {}
    for app in r:
        newBox = InstallButton(apps, text=app)
        newBox.app = str(app)
        newBox.config(command=functools.partial(UnInstall, app))
        newBox.pack()
    apps.geometry("200x500")
    print("Browsing stopped")
    root.deiconify() 

class InstallButton(tk.Button):
    app=""
    def Install(self):
        '''Shows the application information located in /data/application.txt'''
        os.system("python installer.py " + app)

#Window Setup
root = tk.Tk() #Create main window
root.title("OpenStore") #For identification
root.geometry("200x500")
tk.Label(root, text="OpenStore").pack() #Label, so that people know where they are
tk.Button(root, text="Info", command=ShowInfo).pack()
tk.Button(root, text="Browse apps to install", command=BrowseInstall).pack()
tk.Button(root, text="Remove apps", command=BrowseRemove).pack()







root.mainloop()