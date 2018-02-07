#!/usr/bin/env python

import csv
import random

from PIL import Image, ImageTk
import Tkinter as tk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Flshr")
        self.window.geometry("1000x1000")
        self.window.configure(background='grey')
        self.text = ""
        self.imageFile = "data/flshr_images/flshr.jpeg"
        
        windowX = 700
        windowY = 700
        
        path = getattr(sys, '_MEIPASS', os.getcwd())
        os.chdir(path)
        
        with open('data/dicts/dict.csv', mode='r') as infile:
            reader = csv.reader(infile, delimiter='|', quotechar='"')
            tupleList = {(rows[0], rows[1]) for rows in reader}
        
        startImg = ImageTk.PhotoImage(Image.open(self.imageFile).resize((windowY, windowX), Image.ANTIALIAS))
        panel = tk.Label(self.window, image=startImg)
        panel.pack(side="top", fill="both", expand="yes")
        panel.configure(image = startImg)
        panel.image = startImg
        
        entryObj = tk.Entry(self.window)
        entryObj.pack()
        
        def callback(e):
            entryText = entryObj.get().lower().strip()
            
            if (entryText == self.text):
                self.text, self.imageFile = random.sample(tupleList, 1)[0]
                randImg = ImageTk.PhotoImage(Image.open("data/images/" + self.imageFile).resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = randImg)
                panel.image = randImg
            elif (entryText == ""):
                randImg = ImageTk.PhotoImage(Image.open("data/images/" + self.imageFile).resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = randImg)
                panel.image = randImg
            else:
                failImg = ImageTk.PhotoImage(Image.open("data/flshr_images/fail.jpg").resize((windowY, windowX), Image.ANTIALIAS))
                panel.configure(image = failImg)
                panel.image = failImg
            
            entryObj.delete(0, tk.END)
        
        self.window.bind("<Return>", callback)

App().window.mainloop()
