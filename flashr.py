#!/usr/bin/env python

import csv
import random
import time

from Tkinter import *
from PIL import Image, ImageTk

class App:
    def __init__(self, text = ""):
        self.window = Tk()
        self.window.title("Flashr")
        self.window.geometry("1000x1000")
        self.window.configure(background='grey')
        
        windowX = 1000
        windowY = 1000
        
        with open('dict.csv', mode='r') as infile:
            reader = csv.reader(infile, delimiter='|', quotechar='"')
            tupleList = {(rows[0], rows[1]) for rows in reader}
        
        startImg = ImageTk.PhotoImage(Image.open("flashr.jpeg").resize((windowY, windowX), Image.ANTIALIAS))
        panel = Label(self.window, image=startImg)
        panel.pack(side="top", fill="both", expand="yes")
        
        entryObj = Entry(self.window)
        entryObj.pack()
        
        def callback(e):
            global text
            global imageFile
            entryText = entryObj.get()
            
            if (entryText == text):
                text, imageFile = random.sample(tupleList, 1)[0]
                randImg = ImageTk.PhotoImage(Image.open(imageFile).resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = randImg)
                panel.image = randImg
            elif (entryText == ""):
                randImg = ImageTk.PhotoImage(Image.open(imageFile).resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = randImg)
                panel.image = randImg
            else:
                failImg = ImageTk.PhotoImage(Image.open("fail.jpg").resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = failImg)
                panel.image = failImg
            
            entryObj.delete(0, END)
        
        self.window.bind("<Return>", callback)

App().window.mainloop()
