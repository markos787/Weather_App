import tkinter as tk
import requests
import pytz
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
from PIL import Image, ImageTk
from collections import defaultdict


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

    # Weather (from OpenWeather API)
    api='https://api.openweathermap.org/data/2.5/weather?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&units=metric&exclude=hourly&appid=55736dc3bb17f6eba72742b8fe779d5d'
    json_data=requests.get(api).json()
    api_forecast='https://api.openweathermap.org/data/2.5/forecast?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&units=metric&appid=55736dc3bb17f6eba72742b8fe779d5d'
    json_data_for=requests.get(api_forecast).json()

    # Current
    temp=json_data['main']['temp']
    humidity=json_data['main']['humidity']
    pressure=json_data['main']['pressure']
    wind=json_data['wind']['speed']
    descr=json_data['weather'][0]['description']

    temp_res.config(text=(temp, '°C'))
    hum_res.config(text=(humidity, '%'))
    press_res.config(text=(pressure, 'hPa'))
    wind_res.config(text=(wind, 'm/s'))
    desc_res.config(text=descr)

    # Forecast
    icon=[]
    temp_days=[]
    temp_nights=[]
    temps_by_day = defaultdict(list) # creates inserts if they are called but don't exist
    for entry in json_data_for["list"]:
        date = entry["dt_txt"].split(" ")[0]
        temp = entry["main"]["temp"]
        temps_by_day[date].append(temp)
        if '12:00:00' in entry['dt_txt']:
            icon_get=entry['weather'][0]['icon']
            icon.append(icon_get)
    for date, temps in temps_by_day.items():
        temp_max = int(max(temps))
        temp_min = int(min(temps))
        temp_days.append(temp_max)
        temp_nights.append(temp_min)

    # Boxes
    day1_img=icon[0] # returns icon image depending on weather form OpenWeather
    weather_img1=ImageTk.PhotoImage(file=f'icon\\{day1_img}@2x.png')
    image1.config(image=weather_img1)
    image1.image=weather_img1
    temp_day1=temp_days[0]
    temp_night1=temp_nights[0]
    day1_temp.config(text=f'Day: {temp_day1}°C\n Night: {temp_night1}°C')

    day2_img=icon[1]
    img2=Image.open(f'icon\\{day2_img}@2x.png')
    resized_img2=img2.resize((50,50))
    weather_img2=ImageTk.PhotoImage(resized_img2)
    image2.config(image=weather_img2)
    image2.image=weather_img2
    temp_day2=temp_days[1]
    temp_night2=temp_nights[1]
    day2_temp.config(text=f'Day: {temp_day2}°C\n Night: {temp_night2}°C')

    day3_img=icon[2]
    img3=Image.open(f'icon\\{day3_img}@2x.png')
    resized_img3=img3.resize((50,50))
    weather_img3=ImageTk.PhotoImage(resized_img3)
    image3.config(image=weather_img3)
    image3.image=weather_img3
    temp_day3=temp_days[2]
    temp_night3=temp_nights[2]
    day3_temp.config(text=f'Day: {temp_day3}°C\n Night: {temp_night3}°C')

    day4_img=icon[3]
    img4=Image.open(f'icon\\{day4_img}@2x.png')
    resized_img4=img4.resize((50,50))
    weather_img4=ImageTk.PhotoImage(resized_img4)
    image4.config(image=weather_img4)
    image4.image=weather_img4
    temp_day4=temp_days[3]
    temp_night4=temp_nights[3]
    day4_temp.config(text=f'Day: {temp_day4}°C\n Night: {temp_night4}°C')

    day5_img=icon[4]
    img5=Image.open(f'icon\\{day5_img}@2x.png')
    resized_img5=img5.resize((50,50))
    weather_img5=ImageTk.PhotoImage(resized_img5)
    image5.config(image=weather_img5)
    image5.image=weather_img5
    temp_day5=temp_days[4]
    temp_night5=temp_nights[4]
    day5_temp.config(text=f'Day: {temp_day5}°C\n Night: {temp_night5}°C')


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


root=Tk()
root.title("Weather Forecast")
root.geometry('860x470+300+300') # 300 - distance from left and bottom of the screen
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
label1.place(x=40, y=120)

label2=Label(root, text='Humidity', font=('Arial', 11), fg='white', bg='#203243')
label2.place(x=40, y=140)

label3=Label(root, text='Pressure', font=('Arial', 11), fg='white', bg='#203243')
label3.place(x=40, y=160)

label4=Label(root, text='Wind', font=('Arial', 11), fg='white', bg='#203243')
label4.place(x=40, y=180)

label5=Label(root, text='Description', font=('Arial', 11), fg='white', bg='#203243')
label5.place(x=40, y=200)

# Searching box
search_img=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Rounded Rectangle 3.png')
Label(root, image=search_img, bg='dodgerblue').place(x=270, y=120)

weat_img=PhotoImage(file='C:\\Users\\Lenovo\\Pictures\\Nauka\\Programowanie\\Weather_App\\images\\Layer 7.png')
Label(root, image=weat_img, bg='#203243').place(x=290, y=127)

txtfld=tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
txtfld.bind('<Return>', lambda event: get_weather())
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

Label(frame, image=box1, bg='black').place(x=80, y=20) # relative placing (to frame, not root)
Label(frame, image=box2, bg='black').place(x=360, y=30)
Label(frame, image=box2, bg='black').place(x=470, y=30)
Label(frame, image=box2, bg='black').place(x=580, y=30)
Label(frame, image=box2, bg='black').place(x=690, y=30)

# Clock
clock=Label(root, font=('Helvetica', 28, 'bold'), fg='white', bg='dodgerblue')
clock.place(x=30, y=20)

timezone_clock=Label(root, font=('Helvetica', 18, 'bold'), fg='white', bg='dodgerblue')
timezone_clock.place(x=600, y=20)

lon_lat=Label(root, font=('Helvetica', 10), fg='white', bg='dodgerblue')
lon_lat.place(x=600, y=50)

# Forecast results
temp_res=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
hum_res=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
press_res=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
wind_res=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
desc_res=Label(root, font=('Helvetica', 11), fg='white', bg='#203243')

temp_res.place(x=130, y=120)
hum_res.place(x=130, y=140)
press_res.place(x=130, y=160)
wind_res.place(x=130, y=180)
desc_res.place(x=130, y=200)

### Boxes

# First
frame1=Frame(root, width=230, height=132, bg='#203243')
frame1.place(x=85, y=315)

day1=Label(frame1, font='arial 20', bg='#203243', fg='white')
day1.place(x=100, y=3)

image1=Label(frame1, bg='#203243')
image1.place(x=1, y=15)

day1_temp=Label(frame1, font='arial 15 bold', bg='#203243', fg='dodgerblue') # another way to define font
day1_temp.place(x=80, y=50)

# Second
frame2=Frame(root, width=70, height=115, bg='#203243')
frame2.place(x=365, y=325)

day2=Label(frame2, bg='#203243', fg='white')
day2.place(x=10, y=3)

image2=Label(frame2, bg='#203243')
image2.place(x=7, y=20)

day2_temp=Label(frame2, bg='#203243', fg='white')
day2_temp.place(x=2, y=70)

# Third
frame3=Frame(root, width=70, height=115, bg='#203243')
frame3.place(x=475, y=325)

day3=Label(frame3, bg='#203243', fg='white')
day3.place(x=10, y=3)

image3=Label(frame3, bg='#203243')
image3.place(x=7, y=20)

day3_temp=Label(frame3, bg='#203243', fg='white')
day3_temp.place(x=2, y=70)

# Fourth
frame4=Frame(root, width=70, height=115, bg='#203243')
frame4.place(x=585, y=325)

day4=Label(frame4, bg='#203243', fg='white')
day4.place(x=10, y=3)

image4=Label(frame4, bg='#203243')
image4.place(x=7, y=20)

day4_temp=Label(frame4, bg='#203243', fg='white')
day4_temp.place(x=2, y=70)

# Fifth
frame5=Frame(root, width=70, height=115, bg='#203243')
frame5.place(x=695, y=325)

day5=Label(frame5, bg='#203243', fg='white')
day5.place(x=10, y=3)

image5=Label(frame5, bg='#203243')
image5.place(x=7, y=20)

day5_temp=Label(frame5, bg='#203243', fg='white')
day5_temp.place(x=2, y=70)


root.mainloop()