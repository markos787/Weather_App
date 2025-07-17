import tkinter as tk
import requests
import pytz
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
from PIL import Image, ImageTk


root=Tk()
root.title("Weather Forecast")
root.geometry('890x470+300+300') # 300 - distance from left and bottom of the screen
root.configure(bg='dodgerblue')
root.resizable(False, False)

# Icon
im_icon=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\logo.png')
root.iconphoto(False, im_icon) # false - not default

# Image as label
rounded=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Rounded Rectangle 1.png')
Label(root, image=rounded, bg='black').place(x=30, y=110) # place - different way of placing (instead grid with frame)

# Labelling
label1=Label(root, text='Temperature', font=('Arial', 11), fg='white', bg='#203243')
label1.place(x=80, y=120)

label2=Label(root, text='Humidity', font=('Arial', 11), fg='white', bg='#203243')
label2.place(x=80, y=140)

label3=Label(root, text='Pressure', font=('Arial', 11), fg='white', bg='#203243')
label3.place(x=80, y=160)

label4=Label(root, text='Wind', font=('Arial', 11), fg='white', bg='#203243')
label4.place(x=80, y=180)

label5=Label(root, text='Description', font=('Arial', 11), fg='white', bg='#203243')
label5.place(x=80, y=200)

# Searching box
search_img=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Rounded Rectangle 3.png')
Label(root, image=search_img, bg='dodgerblue').place(x=270, y=120)

weat_img=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Layer 7.png')
Label(root, image=weat_img, bg='#203243').place(x=290, y=127)

txtfld=tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
txtfld.place(x=370, y=130)
txtfld.focus()

search_icon=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Layer 6.png')
icon_button=Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#203243')
icon_button.place(x=645, y=125)

# Lower box
frame=Frame(root, width=900, height=180, bg='black')
frame.pack(side=BOTTOM) # another way of placing - docking a frame at the bottom

box1=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Rounded Rectangle 2.png')
box2=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Rounded Rectangle 2 copy.png')

Label(frame, image=box1, bg='black').place(x=30, y=20) # relative placing (to frame, not root)
Label(frame, image=box2, bg='black').place(x=300, y=30)
Label(frame, image=box2, bg='black').place(x=400, y=30)
Label(frame, image=box2, bg='black').place(x=500, y=30)
Label(frame, image=box2, bg='black').place(x=600, y=30)
Label(frame, image=box2, bg='black').place(x=700, y=30)
Label(frame, image=box2, bg='black').place(x=800, y=30)

root.mainloop()