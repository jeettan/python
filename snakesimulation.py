# Import Module
from tkinter import *
import random
import time
 
# create root window
root = Tk()

# root window title and dimension
root.title("Square game run")
# Set geometry (widthxheight)
root.geometry('500x500')

canvas = Canvas(root, width=500, height=450)
canvas["bg"] = "black"

canvas.pack(side=BOTTOM)

label = Label(root, text="Snake simulation", font=("Helvetica", 24))
label.pack(side=TOP)

LENGTH = 3
SPEED = 100
color = "purple"
score = 0

arrow_state = 1
snakeSquares = []
snakeCoords = []
stop_flag = False
gameover = True

def setPosition():

    global x1,x2,y1,y2

    x1 = 5
    x2 = x1 + 25
    y1 = 250
    y2 = y1 + 25

def createBody():

    for y in range(0, LENGTH):

        global x1,x2,y1,y2, snakeSquares

        x1 = x1 + 28
        x2 = x1 + 25

        snakeSquares.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=1))
        snakeCoords.append([x1,y1])

def createSnake(event=None):

    global gameover, snakeSquares, snakeCoords, score, arrow_state

    if(gameover==True):

        gameover = False
        score = 0
        arrow_state = 1
        canvas.delete("all")
        snakeSquares = []
        snakeCoords = []
        label.config(text="Snake simulation")

        setPosition()
        createBody()
        spawnFood()

        gameTickManagement()

        checkEaten()
        addCoords()

def right(event=None):
    global x1, x2

    if(x1>500):
        x1 = 0

    canvas.delete(snakeSquares[0])
    snakeSquares.pop(0)
    snakeCoords.pop(0)

    x1 = x1 + 28
    x2 = x1 + 25

    snakeSquares.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=1))
    snakeCoords.append([x1,y1])

def down(event=None):
    
    global y1, y2

    if(y1>450):
        y1=0

    canvas.delete(snakeSquares[0])
    snakeSquares.pop(0)
    snakeCoords.pop(0)

    y1 = y1 + 28
    y2 = y1 + 25

    snakeSquares.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=1))
    snakeCoords.append([x1,y1])

def left(event=None):
    
    global x1, x2

    if(x1<0):
        x2 = 500

    canvas.delete(snakeSquares[0])
    snakeSquares.pop(0)
    snakeCoords.pop(0)

    x2 = x2 - 28
    x1 = x2 - 25
    snakeSquares.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=1))
    snakeCoords.append([x1,y1])

def up(event=None):
    
    global stop_flag, arrow_state
    global y1, y2

    if(arrow_state != 4):
        return

    if(y2<0):
        y2=500

    canvas.delete(snakeSquares[0])
    snakeSquares.pop(0)
    snakeCoords.pop(0)

    y2 = y2 - 28
    y1 = y2 - 25

    snakeSquares.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, width=1))
    snakeCoords.append([x1,y1])

def rightt(event=None):

    global arrow_state

    if(arrow_state==1 or arrow_state==3):
        return
    
    arrow_state = 1


def downn(event=None):

    global arrow_state

    if(arrow_state==2 or arrow_state==4):
        return

    arrow_state = 2

def leftt(event=None):

    global arrow_state

    if(arrow_state==1 or arrow_state==3):
        return

    arrow_state = 3

def upp(event=None):

    global arrow_state

    if(arrow_state==2 or arrow_state==4):
        return

    arrow_state = 4


def gameTickManagement(event=None):

    global x1, y1, gameover

    if(arrow_state==1):
        right()
    elif(arrow_state==2):
        down()
    elif(arrow_state==3):
        left()
    elif(arrow_state==4):
        up()

    if(gameover !=True):
        canvas.after(SPEED, gameTickManagement)

def spawnFood():

    global foodx, foody

    foodx = random.randint(10,480)
    foody = random.randint(1,430)
    canvas.create_oval(foodx, foody, foodx+30, foody+30, fill="blue", width = 3, tag="food")

    
def checkEaten():
    global foodx, foody, x1, y1, score

    if((x1 > (foodx - 25) and x1 < (foodx + 25)) and (y1 > (foody - 25) and y1 < (foody + 25))):
        canvas.delete("food")
        score = score + 1
        label.config(text=score)
        addSnake()
        spawnFood()

    canvas.after(SPEED, checkEaten)

def addSnake():

    k1 = 5
    k2 = k1 + 25
    j1 = 250
    j2 = j1 + 25

    k = canvas.create_rectangle(0, 0, 0, 0, outline="black", fill=color, width=1)
    snakeSquares.insert(0, k)
    snakeCoords.insert(0, [0,0])

def addCoords():

    global x1,y1, gameover

    check = [x1,y1]

    for x in snakeCoords[:-1]:
        if(check == x):
            gameover = True
            print("GAME OVER")
            return

    canvas.after(SPEED, addCoords)

createSnake()

root.bind("<Right>", rightt)
root.bind("<Down>", downn)
root.bind("<Left>", leftt)
root.bind("<Up>", upp)
root.bind("<space>", createSnake)

root.mainloop()

#delete the last block

