from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
import subprocess
import webbrowser
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def open_timer():
    subprocess.Popen(['python', resource_path('timer.py')])

def open_data():
    subprocess.Popen(['python', resource_path('LE-data.py')])

def website_link():
    webbrowser.open("https://www.lymphedema-thailand.com/")

root = Tk()
root.title("Lymphedema App")

img = PhotoImage(file=resource_path("asset/background.png"))
img2 = ImageTk.PhotoImage(Image.open(resource_path("asset/front.jpeg")))

logo = PhotoImage(file=resource_path("asset/logo.png"))
root.iconphoto(False, logo)

root.resizable(False, False)

root.geometry("400x500")

canvas = Canvas(root, width=400, height=500)
canvas.place(x=0,y=0)
canvas.create_image(0, 0, image=img, anchor="nw")

label = Label(root, image = img2, borderwidth=3, relief="solid")
label.grid(column=0, row=0, pady=(40,0), padx=70)

canvas.create_text(200, 260, text="Lymphedema Management App", font=("Helvetica 24 bold"), fill="black")

button = customtkinter.CTkButton(root, text="Timer",fg_color="#c75d55", bg_color="#c75d55", hover_color="black", command=open_timer, corner_radius=0, width= 150, height=30)
button.grid(column=0,row=1, pady=(60,7))

button2 = customtkinter.CTkButton(root, text="Data/Results", hover_color="black", fg_color="#68aec9", command=open_data, width=150, height=30, corner_radius=0)
button2.grid(column=0,row=2, pady=7)

button3 = customtkinter.CTkButton(root, text="Information", fg_color="#79ae61", hover_color="black", border_width=0, command=website_link, width=150, height=30, corner_radius=0)
button3.grid(column=0,row=3, pady=7)

root.mainloop()