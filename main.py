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

    # Boxes
    day1_img=json_data['daily'][0]['weather'][0]['icon'] # returns icon image depending on weather form OpenWeather
    weather_img1=ImageTk.PhotoImage(file=f'icon\\{day1_img}@2x.png')
    image1.config(image=weather_img1)
    image1.image=weather_img1

    day2_img=json_data['daily'][1]['weather'][0]['icon']
    img2=Image.open(f'icon\\{day2_img}@2x.png')
    resized_img2=img2.resize((50,50))
    weather_img2=ImageTk.PhotoImage(resized_img2)
    image2.config(image=weather_img2)
    image2.image=weather_img2

    day3_img=json_data['daily'][2]['weather'][0]['icon']
    img3=Image.open(f'icon\\{day3_img}@2x.png')
    resized_img3=img3.resize((50,50))
    weather_img3=ImageTk.PhotoImage(resized_img3)
    image3.config(image=weather_img3)
    image3.image=weather_img3

    day4_img=json_data['daily'][3]['weather'][0]['icon']
    img4=Image.open(f'icon\\{day4_img}@2x.png')
    resized_img4=img4.resize((50,50))
    weather_img4=ImageTk.PhotoImage(resized_img4)
    image4.config(image=weather_img4)
    image4.image=weather_img4

    day5_img=json_data['daily'][4]['weather'][0]['icon']
    img5=Image.open(f'icon\\{day5_img}@2x.png')
    resized_img5=img5.resize((50,50))
    weather_img5=ImageTk.PhotoImage(resized_img5)
    image5.config(image=weather_img5)
    image5.image=weather_img5

    day6_img=json_data['daily'][5]['weather'][0]['icon']
    img6=Image.open(f'icon\\{day6_img}@2x.png')
    resized_img6=img6.resize((50,50))
    weather_img6=ImageTk.PhotoImage(resized_img6)
    image6.config(image=weather_img6)
    image6.image=weather_img6

    day7_img=json_data['daily'][6]['weather'][0]['icon']
    img7=Image.open(f'icon\\{day7_img}@2x.png')
    resized_img7=img7.resize((50,50))
    weather_img7=ImageTk.PhotoImage(resized_img7)
    image7.config(image=weather_img7)
    image7.image=weather_img7

    # Days
    first=datetime.now()
    day1.config(text=first.strftime('%A')) # %A - day of the week

    second=first+timedelta(days=1)
    day2.config(text=second.strftime('%A'))

    third=first+timedelta(days=2)
    day3.config(text=third.strftime('%A'))

    fourth=first+timedelta(days=3)
    day4.config(text=fourth.strftime('%A'))

    fifth=first+timedelta(days=4)
    day5.config(text=fifth.strftime('%A'))

    sixth=first+timedelta(days=5)
    day6.config(text=sixth.strftime('%A'))

    seventh=first+timedelta(days=6)
    day7.config(text=seventh.strftime('%A'))


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

day1=Label(frame1, font='arial 20', bg='black', fg='white')
day1.place(x=80, y=5)

image1=Label(frame1, bg='black')
image1.place(x=1, y=15)

# Second
frame2=Frame(root, width=70, height=115, bg='black')
frame2.place(x=305, y=325)

day2=Label(frame2, bg='black', fg='white')
day2.place(x=10, y=5)

image2=Label(frame2, bg='black')
image2.place(x=7, y=20)

# Third
frame3=Frame(root, width=230, height=132, bg='black')
frame3.place(x=405, y=325)

day3=Label(frame3, bg='black', fg='white')
day3.place(x=10, y=5)

image3=Label(frame3, bg='black')
image3.place(x=7, y=20)

# Fourth
frame4=Frame(root, width=230, height=132, bg='black')
frame4.place(x=505, y=325)

day4=Label(frame4, bg='black', fg='white')
day4.place(x=10, y=5)

image4=Label(frame4, bg='black')
image4.place(x=7, y=20)

# Fifth
frame5=Frame(root, width=230, height=132, bg='black')
frame5.place(x=605, y=325)

day5=Label(frame5, bg='black', fg='white')
day5.place(x=10, y=5)

image5=Label(frame5, bg='black')
image5.place(x=7, y=20)

# Sixth
frame6=Frame(root, width=230, height=132, bg='black')
frame6.place(x=705, y=325)

day6=Label(frame6, bg='black', fg='white')
day6.place(x=10, y=5)

image6=Label(frame6, bg='black')
image6.place(x=7, y=20)

# Seventh
frame7=Frame(root, width=230, height=132, bg='black')
frame7.place(x=805, y=325)

day7=Label(frame7, bg='black', fg='white')
day7.place(x=10, y=5)

image7=Label(frame7, bg='black')
image7.place(x=7, y=20)

root.mainloop()