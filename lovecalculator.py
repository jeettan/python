from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.geometry("400x200")
root.title("TKINTER LOVE CALCULATOR")

def checkifempty():
    en1 = entrybox.get()
    en2 = entrybox2.get()

    if(en1 == "" and en2 ==""):
        messagebox.showwarning(title=None,message="Both fields are empty")
        return True

    elif(en1 == ""):
        messagebox.showwarning(title=None,message="First field is empty")
        return True

    elif(en2 == ""):
        messagebox.showwarning(title=None,message="Second field is empty")
        return True
    else:
        return False

def printResult(result):
    love_percentage.config(text="Love percentage: " + result + "%")

def calculating():

    en1 = entrybox.get()
    en2 = entrybox2.get()

    if(checkifempty() == True):
        return

    en1 = list(en1)
    en2 = list(en2)

    en1 = [x.lower() for x in en1]
    en2 = [x.lower() for x in en2]

    result = findcount(en1, en2)

    final = calculatePercentage(result)

    printResult(final)

    return

def findcount(en1, en2):

    loves = {'l': "",'o':"",'v':"",'e':"",'s': ""}

    keys = list(loves.keys())

    count = 0

    for key in keys:
        count = 0
        for x in en1:
            if(x==key):
                count=count+1
        for x in en2:
            if(x==key):
                count=count+1
        
        loves[key] = count

    finalcount = 0

    array1 = []
        
    for love in loves:
        array1.append(loves[love])

    newarray = "".join(map(str, array1))

    return newarray

def calculatePercentage(result):
    
    result = list(result)

    print("RESULT: ", result)

    x = len(result)

    newlist = []
    temp = []
    newlist = result

    while(x>2):
            
        temp = newlist
        newlist = []

        for index, item in enumerate(range(0, x-1)):
            first = int(temp[index]) + int(temp[index+1])
            if(len(str(first))>1):
                new = list(str(first))
                for i in new:
                    newlist.append(i)
            else:
                newlist.append(first)

        x = len(newlist)
        print("LENGTH: ", x)
        print(newlist)

    final_result = "".join(str(num) for num in newlist)

    return final_result

frame = Frame(root, bd=2)
frame.pack()

label = Label(root, text="TKINTER LOVE CALCULATOR")
label.pack()

name = Label(root, text="Name:")
name.pack()

entrybox = ttk.Entry(root,width=20)
entrybox.pack()

partner = Label(root, text="Partner's Name:")
partner.pack()

entrybox2 = ttk.Entry(root, width=20)
entrybox2.pack()

calculate = Button(root, text="Submit", command=calculating)
calculate.pack()

love_percentage = Label(root, text="")
love_percentage.pack()

root.mainloop()