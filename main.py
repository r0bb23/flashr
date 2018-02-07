import csv
import random

from Tkinter import *
from PIL import Image, ImageTk

'''
with open('japanese_dict.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter='|', quotechar='"')
    japTupleList = {(rows[0], rows[1]) for rows in reader}

while True:
    text, imageFile = random.sample(japTupleList, 1)[0]
    print text, imageFile
'''

root = Tk()

w = Label(root, text="Flashr")
w.pack()

image = Image.open("image1.png")
photo = ImageTk.PhotoImage(image)

root.mainloop()
