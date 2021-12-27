import tkinter as tk
from tkinter import font
from tkinter.constants import X
from random import randrange
from typing import Counter
root=tk.Tk()
import random
root.geometry("640x700")
frame = tk.Frame()
frame.master.title("Killer Car")
canvas=tk.Canvas(frame)
import winsound
car = tk.PhotoImage(file='img\pu1.png')
Scar_car=tk.PhotoImage(file='img\down1.png')
Scar_car1=tk.PhotoImage(file='img\down2.png')
gass=tk.PhotoImage(file='img\gasss.png')
bg=tk.PhotoImage(file='img\g1.png')
menu=tk.PhotoImage(file='img\Mbg.png')
##==============================menu and background===================================================
numberCoins = 0
mytext=[]
myScore=[]
passed = False
notFinished=True
Grid =[
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,4,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,1,0,0,0,0,2],   
    ]


def displaygrid():
    canvas.delete('all')
    global Grid, notFinished ,myScore
    myScore = 'SCORE: ' + str(numberCoins )
    canvas.create_image (330,350 ,image=bg)
    # canvas.create_text(500,500,text="SCORE:",font=("Pursia",20,"bold"))
    y1 = -285
    y2 = -210
    x1=5
    x2=75
    isTrue=True
    if isTrue and numberCoins!=700:
        for col in Grid:
            for row in col:
                if row==0:
                    canvas.create_rectangle(x1,y1,x2,y2, outline='')
                elif row==1:
                    canvas.create_image((x2-35),y2-35,image=car)
                elif row==3:
                    # canvas.create_image(x2-35,y2-35, image=Scar_car )
                    canvas.create_image(x2-35,y2-35, image=Scar_car1 )
                elif row == 4:
                    canvas.create_image((x2-35),y2-35,image=gass)
                x1=x2
                x2 += 70
            x1 =5
            x2=75
            y1 = y2
            y2 += 70
    elif numberCoins==700:
        gameWin()
    canvas.create_text(100, 50 , text=myScore, font=('consolas', 24, 'bold'), fill='#e0e0e0')
##                                             ENERMY_CAR
##============================================== randomCarRow ============================================
def randomCarRow():
    global storeRow
    storeRow = []
    while len(storeRow) != 3:
        randomRow = randrange(0, 4)
        if randomRow not in storeRow:
            storeRow.append(randomRow)
    randomCarCol()
##================================================randomCarCol==============================================
def randomCarCol():
    global storeNum
    storeNum = []
    while len(storeNum) != 3:
        randNum = randrange(1, 8)
        if randNum not in storeNum:
            storeNum.append(randNum)
    replace()
    # randomCarCol

##===============================================replaceNumberOfcar====================================
def replace():
    global Grid
    for a in range(len(storeRow)):
        Grid[storeRow[a]][storeNum[a]] = 3
    displaygrid()
# #===========================================care_move================================================
def  moveCar():
    global Grid 
    # passed = False
    countCar = 0
    # if not passed:
    
    for col in range(len(Grid)):
            for row in range(len(Grid[col])):
                if Grid[col][row] == 3 and countCar != 3 and col < len(Grid)-1:
                    Grid[col][row] = 0
                    Grid[col+1][row] = 3
                    countCar += 1
                elif Grid[col][row] ==3 and col==len(Grid)-1:
                    Grid[col][row] =0
    displaygrid()
    canvas.after(900,lambda:moveCar())
   
# def rerandomCar():
#     displaygrid()
#     moveCar()
# canvas.after(900,lambda:moveCar())

# def stop(event):
#     global passed
#     passed = True
                                   
def move_gass():
    global Grid
    isHas = False
    for col in range(len(Grid)-1):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 4 and not isHas and Grid[col+1][row] == 0 :
                Grid[col][row] = 0
                Grid[col+1][row] = 4
                isHas = True
            elif Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] != 0 and Grid[col+1][row] == 4:
                Grid[col][row] = 0
                winsound.PlaySound("sound\sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col+1][row] = 1
                countCoins()
            
            
    displaygrid()
    canvas.after(1000,lambda:move_gass())
# --------------countCoins--------------
def countCoins():
    global numberCoins
    numberCoins+=700
print(numberCoins)
##==========================================Start game===================================================
def tostart():
    randomCarRow()
    moveCar()
    move_gass()
    myButton.place_forget()  
    exit.place_forget() 
myButton = tk.Button(root, text="Start",command=tostart)
myButton.config(width=7, height=1, bg="blue",fg="yellow",border="3",  font=("Arial", 20, "bold"))
myButton_canvas = canvas.create_window(630, 450, anchor="nw", window=myButton, tags="button")
myButton.pack()
myButton.place(x=180,y=450)

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.config(width=7, height=1, bg="blue",fg="yellow",border="3",font=("Arial", 20, "bold"))
exit_canvas = canvas.create_window(630, 520, anchor="nw", window=exit)
exit.pack()
exit.place(x=350,y=450)
canvas.create_image(318,350 ,image=menu)   

##=======================win and lost game===============================
Islose = True
isWin = True
def gameOver():
    global Islose
    if Islose:
        Islose=False
        winsound.PlaySound("sound\gameover1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def gameWin():
    global isWin
    canvas.create_image(320,350 ,image=win)
   
    winsound.PlaySound("sound\win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
  
# def clean():
#     global Grid
#     Grid = []
#     displaygrid()

# def yourScore():
#     global countCoins, notFinished
#     if not notFinished:
#         canvas.delete('all')
#         if countCoins != 700:
#             canvas.create_image(0, 0, image=over, anchor='nw')
#             canvas.create_text(600,450, text="Your Score "+str(countCoins), font=(('couriernew'), 38, 'bold'), fill='#2196f3')
#             gameOver()
#         else:
#             canvas.create_image(0, 0, image=win, anchor='nw')
#             canvas.create_text(600, 470, text="YOU WIN", font=(('consolas'), 48, 'bold'), fill='#b71c1c')
#             gameWin()
##=============================================end win and lost============================================
##============ =================================move_care to right==========================================
def move_right(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and row < len(Grid[col])-1 and Grid[col][row+1]!=2:
                Grid[col][row] = 0      
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row+1] = 1
                isHas =True 
    displaygrid()
root.bind("<Right>", move_right)

##============================================= move_care to left============================================
def move_left(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and row > 0 and Grid[col][row-1]!=2:
                Grid[col][row] = 0
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row-1] = 1
                isHas =True  
    displaygrid() 
root.bind("<Left>", move_left)

##============================================== move_care to down===========================================
def move_down(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and col < len(Grid)-1:
                Grid[col][row] = 0
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col+1][row] = 1
                isHas =True
    
    displaygrid()
root.bind("<Down>", move_down)

##============================================== move_care to down============================================
def move_up(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] == 0 and Grid[col-1][row] != 4:
                Grid[col][row] = 0
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col-1][row] = 1
                isHas =True
            elif Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] != 0 and Grid[col-1][row] == 4:
                Grid[col][row] = 0
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col-1][row] = 1
                countCoins()
            
    displaygrid()
root.bind("<Up>", move_up)
# root.bind("<p>",stop)
over=tk.PhotoImage(file='img\over.png')
win=tk.PhotoImage(file='img\win.png')
frame.pack(expand=True ,fill='both')
canvas.pack(expand=True ,fill='both')
root.mainloop()


















# import tkinter as tk
# from tkinter.constants import X
# from random import randrange
# from typing import Counter
# root=tk.Tk()
# import random
# root.geometry("640x700")
# frame = tk.Frame()
# frame.master.title("Killer Car")
# canvas=tk.Canvas(frame)
# import winsound
# car = tk.PhotoImage(file='img\pu1.png')
# Scar_car=tk.PhotoImage(file='img\down1.png')
# Scar_car1=tk.PhotoImage(file='img\down2.png')
# gass=tk.PhotoImage(file='img\gasss.png')
# bg=tk.PhotoImage(file='img\g1.png')
# menu=tk.PhotoImage(file='img\Mbg.png')
# ##==============================menu and background===================================================
# Countscore = 0 
# mytext=[]
# passed = False
# Grid =[
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,4,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,0,0,0,0,0,2],
#         [2,0,0,1,0,0,0,0,2],   
#     ]


# def displaygrid():
#     canvas.delete('all')
#     canvas.create_image (330,350 ,image=bg)
#     global Grid
#     y1 = -285
#     y2 = -210
#     x1=5
#     x2=75
#     for col in Grid:
#         for row in col:
#             if row==0:
#                 canvas.create_rectangle(x1,y1,x2,y2, outline='')
#             elif row==1:
#                 canvas.create_image((x2-35),y2-35,image=car)
#             elif row==3:
#                 # canvas.create_image(x2-35,y2-35, image=Scar_car )
#                 canvas.create_image(x2-35,y2-35, image=Scar_car1 )
#             elif row == 4:
#                 canvas.create_image((x2-35),y2-35,image=gass)
            
#             x1=x2
#             x2 += 70
#         x1 =5
#         x2=75
#         y1 = y2
#         y2 += 70
# ##                                             ENERMY_CAR
# ##============================================== randomCarRow ============================================
# def randomCarRow():
#     global storeRow
#     storeRow = []
#     while len(storeRow) != 3:
#         randomRow = randrange(0, 4)
#         if randomRow not in storeRow:
#             storeRow.append(randomRow)
#     randomCarCol()
# ##================================================randomCarCol==============================================
# def randomCarCol():
#     global storeNum
#     storeNum = []
#     while len(storeNum) != 3:
#         randNum = randrange(1, 8)
#         if randNum not in storeNum:
#             storeNum.append(randNum)
#     replace()
#     # randomCarCol

# ##===============================================replaceNumberOfcar====================================
# def replace():
#     global Grid
#     for a in range(len(storeRow)):
#         Grid[storeRow[a]][storeNum[a]] = 3
#     displaygrid()
# # #===========================================care_move================================================
# def  moveCar():
#     global Grid ,passed
#     passed = False
#     countCar = 0
#     if not passed:
    
#         for col in range(len(Grid)):
#             for row in range(len(Grid[col])):
#                 if Grid[col][row] == 3 and countCar != 3 and col < len(Grid)-1:
#                     Grid[col][row] = 0
#                     Grid[col+1][row] = 3
#                     countCar += 1
#                 elif Grid[col][row] ==3 and col==len(Grid)-1:
#                     Grid[col][row] =0
#         displaygrid()
#     canvas.after(900,lambda:moveCar())
   
# # def rerandomCar():
# #     displaygrid()
# #     moveCar()
# # canvas.after(900,lambda:moveCar())

# def stop(event):
#     global passed
#     passed = True
                                   
# def move_gass():
#     global Grid
#     isHas = False
#     for col in range(len(Grid)-1):
#         for row in range(len(Grid[col])):
#             if Grid[col][row] == 4 and not isHas :
#                 Grid[col][row] = 0
#                 Grid[col+1][row] = 4
#                 isHas = True
            
#     displaygrid()
#     canvas.after(1000,lambda:move_gass())

# ##==========================================Start game===================================================
# def tostart():
#     randomCarRow()
#     moveCar()
#     move_gass()
#     myButton.place_forget()  
#     exit.place_forget() 
# myButton = tk.Button(root, text="Start",command=tostart)
# myButton.config(width=7, height=1, bg="blue",fg="yellow",border="3",  font=("Arial", 20, "bold"))
# myButton_canvas = canvas.create_window(630, 450, anchor="nw", window=myButton, tags="button")
# myButton.pack()
# myButton.place(x=180,y=450)

# exit = tk.Button(root, text="Exit", command=root.destroy)
# exit.config(width=7, height=1, bg="blue",fg="yellow",border="3",font=("Arial", 20, "bold"))
# exit_canvas = canvas.create_window(630, 520, anchor="nw", window=exit)
# exit.pack()
# exit.place(x=350,y=450)
# canvas.create_image(318,350 ,image=menu)   




# ##============ =================================move_care to right==========================================
# def move_right(event):
#     global Grid
#     isHas = False
#     for col in range(len(Grid)):
#         for row in range(len(Grid[col])):
#             if Grid[col][row] == 1 and not isHas and row < len(Grid[col])-1 and Grid[col][row+1]!=2:
#                 Grid[col][row] = 0      
#                 winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#                 Grid[col][row+1] = 1
#                 isHas =True 
#     displaygrid()
# root.bind("<Right>", move_right)

# ##============================================= move_care to left============================================
# def move_left(event):
#     global Grid
#     isHas = False
#     for col in range(len(Grid)):
#         for row in range(len(Grid[col])):
#             if Grid[col][row] == 1 and not isHas and row > 0 and Grid[col][row-1]!=2:
#                 Grid[col][row] = 0
#                 winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#                 Grid[col][row-1] = 1
#                 isHas =True  
#     displaygrid() 
# root.bind("<Left>", move_left)

# ##============================================== move_care to down===========================================
# def move_down(event):
#     global Grid
#     isHas = False
#     for col in range(len(Grid)):
#         for row in range(len(Grid[col])):
#             if Grid[col][row] == 1 and not isHas and col < len(Grid)-1:
#                 Grid[col][row] = 0
#                 winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#                 Grid[col+1][row] = 1
#                 isHas =True
    
#     displaygrid()
# root.bind("<Down>", move_down)

# ##============================================== move_care to down============================================
# def move_up(event):
#     global Grid
#     isHas = False
#     for col in range(len(Grid)):
#         for row in range(len(Grid[col])):
#             if Grid[col][row] == 1 and not isHas and col>5:
#                 Grid[col][row] = 0
#                 winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#                 Grid[col-1][row] = 1
#                 isHas =True
#             # if Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] == 4:
#             #     score()
#     displaygrid()
# root.bind("<Up>", move_up)
# root.bind("<p>",stop)
# frame.pack(expand=True ,fill='both')
# canvas.pack(expand=True ,fill='both')
# root.mainloop()


































