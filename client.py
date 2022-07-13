import socket
from threading import Thread
from tkinter import *
from PIL import ImageTk,Image
import random


screen_width=None
screen_height=None

SERVER=None
PORT=None
IP_ADDRESS=None

canvas1=None
playerName=None
nameEntry=None
nameWindow=None

gameWindow=None
dice=None

leftBoxes = []
rightBoxes = []
finishingBox = None

def leftBoard():
    global gameWindow
    global leftBoxes
    global screen_height

    xPos = 30
    for box in range(0,11):
        if(box == 0):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=0, bg="red")
            boxLabel.place(x=xPos, y=screen_height/2 - 88)
            leftBoxes.append(boxLabel)
            xPos +=50
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",55), width=2, height=1, relief='ridge', borderwidth=0, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2- 100)
            leftBoxes.append(boxLabel)
            xPos +=75


def rightBoard():
    global gameWindow
    global rightBoxes
    global screen_height

    xPos = 988
    for box in range(0,11):
        if(box == 10):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=0, bg="yellow")
            boxLabel.place(x=xPos, y=screen_height/2-88)
            rightBoxes.append(boxLabel)
            xPos +=50
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",55), width=2, height=1, relief='ridge', borderwidth=0, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2 - 100)
            rightBoxes.append(boxLabel)
            xPos +=75

def finishingBox():
    global gameWindow
    global finishingBox
    global screen_width
    global screen_height

    finishingBox = Label(gameWindow, text="Home", font=("Chalkboard SE", 32), width=8, height=4, borderwidth=0, bg="green", fg="white")
    finishingBox.place(x=screen_width/2 - 68, y=screen_height/2 -160)




def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    

    SERVER.send(playerName.encode())
    gameWindow()

def askPlayerName():
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow=Tk()
    nameWindow.title("LUDO LADDER")
    nameWindow.attributes("-fullscreen",True)

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./background.png")

    canvas1=Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2+20,screen_height/5,text="Enter your Name",font=("Calibri",50),fill="white")

    # nameEntry=Entry(nameWindow,width=15,justify='center',font=("Calibri",50),bd=5,bg='white')
    # nameEntry.place(x=screen_width/2 - 220,y=screen_height/4 +150)

    

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.pack()
    # nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 150)

   

    button=Button(nameWindow,text="save",font=("Calibri",50),width=8,height=1,bg="lightblue",bd=3,command=saveName)
    button.place(x=screen_width/2 - 130,y=screen_height/2 +100)

    exit_button=Button(nameWindow,text="Exit",command=nameWindow.destroy)
    exit_button.place(x=screen_width/2 - 250,y=screen_height/2+250)

    
    nameWindow.resizable(True,True)
    nameWindow=mainloop()

    

def gameWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice

    gameWindow=Tk
    gameWindow.title("Ludo Lader Game")
    gameWindow.attributes(".-fullscreen",True)

    screen_width=gameWindow.winfo_screenwidth()
    screen_height=gameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./background.png")

    canvas2=Canvas(gameWindow,width=500,height=500)
    canvas2.pack(fill="both",expand=True)

    canvas2.create_image(0,0,image=bg,anchor="nw")
    canvas2.create_text(screen_width/2+20,screen_height/5,text="Enter your Name",font=("Calibri",50),fill="white")

    gameWindow.resizable(True,True)
    gameWindow=mainloop()

    leftBoard()
    rightBoard()


    finishingBox()



        


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 8000

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    askPlayerName()

setup()
