#Openstore app. GUI handler
#IMPORTANT FILE! READ CHANGES THROUGH CAREFULLY!

#TODO
#Add simple GUI
#Add downloading


#Module importing
import tkinter as tk #Importing tkinter in order to create GUI. Calling it tk because it is easy to remember and short
from tkinter import messagebox#Import messagebox, so that we can display info
import os #For info

#Function Defintion
def ShowInfo():
    '''Shows the application information located in /data/application.txt'''
    messagebox.showinfo(title="Information", message=open("data/application.txt", "r").read())



#Window Setup
root = tk.Tk() #Create main window
root.title("OpenStore") #For identification
root.geometry("200x500")
tk.Label(root, text="OpenStore").pack() #Label, so that people know where they are
tk.Button(root, text="Info", command=ShowInfo).pack()







root.mainloop()