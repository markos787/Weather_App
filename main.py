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



root.mainloop()