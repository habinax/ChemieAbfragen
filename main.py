import tkinter as tk
from tkinter import filedialog

from gui import MyGUI
from PIL import Image, ImageTk
from os import listdir
import random
from PyPDF2 import PdfReader
# creating a pdf reader object
#reader = PdfReader('C:\\Users\\inap\\Downloads\\chemiemol\\printtopdf.pdf')



# import PySimpleGUI as psg
#
# answer_column = [
#
#     [psg.Button(dic[0][1])],
#
#     [psg.Button(dic[1][1])],
#
#     [psg.Button(dic[2][1])]
#
# ]
#
# layout = [
#     [
#         psg.Image(dic[0][0], expand_x=True, expand_y=True),
#         psg.VSeperator(),
#         psg.Column(answer_column),
#     ]
# ]

root = tk.Tk()
app = MyGUI(root)
root.geometry("800x300")  # Setze die gewünschte Startgröße
root.mainloop()

# layout = [[psg.Image(dic[0][0],
#    expand_x=True, expand_y=True)],
#           [psg.Column([psg.Button(dic[0][1])],
#             [psg.Button(dic[1][1])])]
# ]
# ###Setting Window

#window = psg.Window('Der Molekülspaß ist real', layout, size=(400,400), resizable = True)

###Showing the Application, also GUI functions can be placed here.
# while True:
#     event, values = window.read()
#     if event == psg.WIN_CLOSED or event == "Exit":
#         break

#window.close()


# from spire.pdf.common import *
# from spire.pdf import *
#
# # Create a PdfDocument object
# doc = PdfDocument()
#
# # Load a PDF document
# doc.LoadFromFile('C:\\Users\\inap\\Downloads\\chemiemol\\printtopdf.pdf')
#
# images = []
#
# # Loop through the pages in the document
# for i in range(doc.Pages.Count):
#     page = doc.Pages.get_Item(i)
#
#     # Extract images from a specific page
#     for image in page.ExtractImages():
#         images.append(image)
#
# # Save images to specified location with specified format extension
# index = 0
# for image in images:
#     imageFileName = 'C:\\Users\\inap\\PycharmProjects\\ChemieAbfragen\\venv\\Picturesprinttopdf\\mol-{}.png'.format(index)
#     index += 1
#     image.Save(imageFileName, ImageFormat.get_Png())
# doc.Close()