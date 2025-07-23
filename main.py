import tkinter as tk
import requests
import pytz
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
from PIL import Image, ImageTk


def get_weather():

    # Time and timezone
    city=txtfld.get()
    locator=Nominatim(user_agent='geoapiExcercises') # calling an object
    location=locator.geocode(city) # converting city name to coordinates
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone_clock.config(text=result)
    if location.latitude>=0:
        ns='N'
        lat=round(location.latitude, 4)
    else:
        ns='S'
        lat=(-1)*round(location.latitude, 4)
    if location.longitude>=0:
        ew='E'
        lon=round(location.longitude, 4)
    else:
        ew='W'
        lon=(-1)*round(location.longitude, 4)
    lon_lat.config(text=f'{lat}°{ns}, {lon}°{ew}')
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%H:%M') # H - time in 24h system
    clock.config(text=current_time)

    # Weather (from OpenWeather API, creating API key is paid)
    api='https://api.openweathermap.org/data/2.5/onecall?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&units=metric&exclude=hourly&appid={API key}'
    json_data=requests.get(api).json()

    # Current
    temp=json_data['current']['temp']
    humidity=json_data['current']['humidity']
    pressure=json_data['current']['pressure']
    wind=json_data['current']['wind_speed']
    descr=json_data['current']['weather'][0]['description']

    temp_res.config(text=(temp, '°C'))
    hum_res.config(text=(humidity, '%'))
    press_res.config(text=(pressure, 'hPa'))
    wind_res.config(text=(wind, 'm/s'))
    desc_res.config(text=descr)

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
icon_button=Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#203243', command=get_weather)
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

# Clock
clock=Label(root, font=('Helvetica', 28, 'bold'), fg='white', bg='dodgerblue')
clock.place(x=30, y=20)

timezone_clock=Label(root, font=('Helvetica', 18, 'bold'), fg='white', bg='dodgerblue')
timezone_clock.place(x=600, y=20)

lon_lat=Label(root, font=('Helvetica', 10), fg='white', bg='dodgerblue')
lon_lat.place(x=600, y=50)

# Forecast results
temp_res=Label(root, text='temp', font=('Helvetica', 11), fg='white', bg='#203243')
hum_res=Label(root, text='temp', font=('Helvetica', 11), fg='white', bg='#203243')
press_res=Label(root, text='temp', font=('Helvetica', 11), fg='white', bg='#203243')
wind_res=Label(root, text='temp', font=('Helvetica', 11), fg='white', bg='#203243')
desc_res=Label(root, text='temp', font=('Helvetica', 11), fg='white', bg='#203243')

temp_res.place(x=150, y=120)
hum_res.place(x=150, y=140)
press_res.place(x=150, y=160)
wind_res.place(x=150, y=180)
desc_res.place(x=150, y=200)

### Boxes

# First
frame1=Frame(root, width=230, height=132, bg='black')
frame1.place(x=35, y=315)

# Second
frame2=Frame(root, width=70, height=115, bg='black')
frame2.place(x=305, y=325)

# Third
frame3=Frame(root, width=230, height=132, bg='black')
frame3.place(x=405, y=325)

# Fourth
frame4=Frame(root, width=230, height=132, bg='black')
frame4.place(x=505, y=325)

# Fifth
frame5=Frame(root, width=230, height=132, bg='black')
frame5.place(x=605, y=325)

# Sixth
frame6=Frame(root, width=230, height=132, bg='black')
frame6.place(x=705, y=325)

# Seventh
frame7=Frame(root, width=230, height=132, bg='black')
frame7.place(x=805, y=325)

root.mainloop()