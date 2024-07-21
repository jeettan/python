import customtkinter
from tkinter import *
from tkinter import messagebox

root = customtkinter.CTk()
root.geometry("400x450")
root.title("Phone book create")

customtkinter.set_appearance_mode("Dark") 

datas = []

def checkifempty():

    if(entry1.get()=="" or entry2.get()== "" or entry3.get() ==""):
        messagebox.showwarning(title="Empty fields", message="ERROR. Empty fields.")
        return True
    
    elif(not entry3.get().isnumeric()):
        print("Not numeric number")
        messagebox.showwarning(title="Not numeric", message="ERROR. Enter a valid phone number")
        return True

def add():
    if(checkifempty()):
        return
    datas.append([entry1.get(),entry2.get(),entry3.get()])
    listbox.insert("end", entry1.get())

def delete():
    x = listbox.curselection()[0]
    listbox.delete(listbox.curselection()[0])
    del datas[int(x)]

def view():
    global datas
    x = listbox.curselection()[0]
    Full_Name.set(datas[x][0])
    Nick_Name.set(datas[x][1])
    Phone_Number.set(datas[x][2])

def clear():
    Full_Name.set("")
    Nick_Name.set("")
    Phone_Number.set("")

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def tab_two():
    global datas
    delete_pages()
    new_frame = customtkinter.CTkFrame(main_frame)
    new_frame.pack(side=TOP)
    new_frame.configure(width=400, height=400)

    for x in datas:
        lb = customtkinter.CTkLabel(new_frame, text= f"{x[0]}, {x[1]}, {x[2]}", text_color="white")
        lb.pack()
    new_frame.pack()

def home():

    global entry1, entry2, entry3, listbox, Full_Name, Nick_Name, Phone_Number

    delete_pages()

    frame = customtkinter.CTkFrame(main_frame)
    frame.pack(pady=5)

    scrollbar = Scrollbar(frame, orient=VERTICAL)

    listbox = Listbox(frame, yscrollcommand=scrollbar.set) 
    listbox.pack(side=LEFT, fill=BOTH, expand=True) 

    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    frame1 = customtkinter.CTkFrame(main_frame)
    frame1.pack(pady=5)
    frame2 = customtkinter.CTkFrame(main_frame)
    frame2.pack(pady=5)
    frame3 = customtkinter.CTkFrame(main_frame)
    frame3.pack(pady=5)
    frame4 = customtkinter.CTkFrame(main_frame)
    frame4.pack(pady=5)

    Full_Name = StringVar()
    Nick_Name = StringVar()
    Phone_Number = StringVar()

    customtkinter.CTkLabel(frame1, text="Full Name").pack(side=LEFT, padx=10)
    entry1 = customtkinter.CTkEntry(frame1, placeholder_text="Name", textvariable=Full_Name)
    entry1.pack()

    customtkinter.CTkLabel(frame2, text="Nick Name").pack(side=LEFT, padx=10)
    entry2 = customtkinter.CTkEntry(frame2, placeholder_text="Nick Name", textvariable=Nick_Name)
    entry2.pack()

    customtkinter.CTkLabel(frame3, text="Phone Number").pack(side=LEFT, padx=10)
    entry3 = customtkinter.CTkEntry(frame3, placeholder_text="Phone Number", textvariable=Phone_Number)
    entry3.pack()

    add_button = customtkinter.CTkButton(frame4, text="Add", width=40, command=add)
    add_button.pack(side=LEFT, padx=10)

    view_button = customtkinter.CTkButton(frame4, text="View", width=40, command=view)
    view_button.pack(side=LEFT, padx=10)
    delete_button = customtkinter.CTkButton(frame4, text="Delete", width=40, command=delete)
    delete_button.pack(side=LEFT, padx=10)
    clear_button = customtkinter.CTkButton(frame4, text="Clear", width=40, command=clear)
    clear_button.pack(side=LEFT, padx=10)

    for item in datas:
        listbox.insert("end", item[0])

option_frame = customtkinter.CTkFrame(root)
option_frame.pack(side=TOP)
option_frame.configure(width=400, height=50)

firstoption = customtkinter.CTkButton(option_frame, text="Home", fg_color="transparent", hover=False, command=home)
firstoption.pack(side=LEFT)

secondoption = customtkinter.CTkButton(option_frame, text="Tab 2", fg_color="transparent", hover=False, command=tab_two)
secondoption.pack()

main_frame = customtkinter.CTkFrame(root)
main_frame.pack(side=TOP)
main_frame.configure(width=400, height=400)

home()

root.mainloop()