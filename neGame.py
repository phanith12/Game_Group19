import tkinter as tk
import random
from typing import TYPE_CHECKING
import winsound
root=tk.Tk()
root.geometry("640x700")
root.title('KILLER CAR')
canvas = tk.Canvas(root)
back=tk.PhotoImage(file='img\BG.png')

#-----------------+VARIABLE*------------------------------------------------------#
durationOfCarToMove = 0
isCan=True
numberCoins = 0
grid=[
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,4,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,1,0,0,0,0,2]   
    ]
#-----------------*CREATE FUNTION TO MAKE BUTTON START GAME*------------------------#
def start():
    displayGrid()
    moveCar()
    movePoint()
    myButton.place_forget()  
    exit.place_forget() 
 
#-------------------------*CREATE FUNTION TO DISPLAY SQUARE*--------------------------#
def displayGrid():
    canvas.delete('all')
    global grid,notFinished , myScore
    myScore= 'SCORE: ' + str(numberCoins)
    canvas.create_image (330,350 ,image=bg)

    y1 = -285
    y2 = -210
    x1 = 5
    x2 = 75
    isTrue = True
    if isTrue and numberCoins < 700:
        for col in grid:
            for row in col:
                if row == 0:
                    canvas.create_rectangle(x1,y1,x2,y2, outline='')
                elif row == 1:
                    canvas.create_image(x2-35,y2-35, image=car)
                elif row == 2 :
                    canvas.create_rectangle(x1,y1,x2,y2, outline='')
                elif row == 3:
                    canvas.create_image(x2-35,y2-35, image=scarCar)
                elif row == 4:
                    canvas.create_image(x2-35,y2-35, image=gass)

                x1=x2
                x2 += 70
            x1 =5
            x2=75
            y1 = y2
            y2 += 70 
    elif numberCoins ==700:
        gameWin()
    else:
        gameOver()
    canvas.create_text(100, 50 , text=myScore, font=('consolas', 24, 'bold'), fill='#e0e0e0')
    
#----------------------------*CREATE FUNTION TO DROP_CAR*-----------------------------#
def  moveCar():
    global grid, durationOfCarToMove
    durationOfCarToMove += 1
    isTrue = False
    for col in range (len(grid)):
        for row in range(len (grid[col])):
                if grid[col][row] == 3  and col < len(grid)-1 and not isTrue :
                    grid[col][row] = 0
                    grid[col+1][row] = 3
                    isTrue=True
                elif grid[col][row] ==3 and col==len(grid)-1 :
                    grid[col][row] =0
    displayGrid()
    canvas.after(500,lambda:moveCar())
#----------------------------*CREATE FUNTION TO RANDOM_CAR*---------------------------# 
def randomCar():
    global grid
    numCol = random.randrange(1,8)
    grid[0][numCol] = 3
randomCar()

#----------------------------*CREATE FUNTION TO DROP_POINT*---------------------------#
def movePoint():
    isTrue = False
    global grid
    for col in range (len(grid)):
        for row in range(len (grid[col])):
                if grid[col][row] == 4  and col < len(grid)-1 and not isTrue:
                    grid[col][row] = 0
                    grid[col+1][row] = 4
                    isTrue = True
                elif grid[col][row] ==4 and col==len(grid)-1 :
                    grid[col][row] =0
                elif grid[col][row] == 1 and not isTrue and col>5 and grid[col-1][row] != 0 and grid[col+1][row] == 4:
                    grid[col][row] = 0
                    grid[col+1][row] = 1
                    countCoins()
    displayGrid()
    canvas.after(300,lambda:movePoint())

#----------------------------*CREATE FUNTION TO COUNTCOINS*---------------------------#
def countCoins():
    global numberCoins
    numberCoins+=700

#---------------------------------CREATE BUTTON--------------------------------------#
myButton = tk.Button(root, text="Start",command=start)
myButton.config(width=7, height=1, bg="blue",fg="yellow",border="3",  font=("Arial", 20, "bold"))
myButton_canvas = canvas.create_window(630, 450, anchor="nw", window=myButton, tags="button")
myButton.pack()
myButton.place(x=170,y=400)

exit = tk.Button(root, text="Exit", command=root.destroy)
exit.config(width=7, height=1, bg="blue",fg="yellow",border="3",font=("Arial", 20, "bold"))
exit_canvas = canvas.create_window(630, 520, anchor="nw", window=exit)
exit.pack()
exit.place(x=350,y=400)
canvas.create_image(318,350 ,image=back) 
canvas.create_text(300, 50, text='KILLER CAR !' , font=("Arial", 25, "bold") , fill= '#f39c12')
canvas.create_text(300, 110, text='Welcome to my game' , font=("Arial", 20) , fill= '#95a5a6')
canvas.create_text(300, 190, text='Explaining ' , font=("Arial", 18 , "bold") , fill= '#bdc3c7')
canvas.create_text(300, 290, text='1/ Player can move car by key Up, Down, Left, Right \n \n 2/ If car player hit the gass you will increase point. \n \n 3/ If car player hit anovther car will lost. ' , font=("Arial", 15), fill= 'white')
#----------------------------*CREATE FUNTION TO DEFIND WIN OR LOST*---------------------#
def gameOver():
    canvas.create_image(320,350 ,image=ver)
    winsound.PlaySound("sound\gameover1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_text (300, 500 , text='Game over' ,fill='black' )
def gameWin():
    canvas.create_image(320,350 ,image=win)
    winsound.PlaySound("sound\win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)  
def defeat():
    global isCan
    if isCan :
        displayGrid()
    else:
        gameOver()
#----------------------------*CREATE FUNTION TO MOVE POSTION*---------------------------#
def movePosition(move):
    isHas =False
    global isCan
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if move== 'Right': 
                if grid[col][row] == 1 and not isHas and grid[col][row+1]!=2 :
                    winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                    grid[col][row] = 0      
                    grid[col][row+1] = 1
                    isHas =True 
            if  move == 'Left':
                if grid[col][row] == 1  and grid[col][row-1]!=2:
                    winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                    grid[col][row] = 0
                    grid[col][row-1] = 1
                    isHas =True  
            if   move == 'Down':
                if grid[col][row] == 1  and not isHas and col < len(grid)-1:
                    winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                    grid[col][row] = 0
                    grid[col+1][row] = 1
                    isHas =True
            if  move=='Up':
                if grid[col][row] == 1 and not isHas and col >9 and grid[col-1][row] == 0:
                    winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                    grid[col][row] = 0
                    grid[col-1][row] = 1
                    isHas =True
                elif grid[col][row] == 1 and not isHas and col>5 and grid[col-1][row] != 0 and grid[col-1][row] == 4:
                    grid[col][row] = 0
                    grid[col-1][row] = 1
                    countCoins()
                elif grid[col][row] == 1 and not isHas  and grid[col-1][row] == 3:
                    isCan=False
        defeat()
#-----------*CREATE BLOCK FUNTION TO MOVE (LEFT , RIGHT, UP , DOWN)*--------------------#
def moveRight(event):
    movePosition('Right')
def moveLeft(event):
    movePosition('Left')
def moveDown(event):
    movePosition('Down')
def moveUp(event):
    movePosition('Up')
#----------------------------------BLOCK_IMAGE-----------------------------------------#
scarCar=tk.PhotoImage(file='img\down1.png')
car = tk.PhotoImage(file='img\pu1.png')
gass=tk.PhotoImage(file='img\gasss.png')
ver=tk.PhotoImage(file='img\er.png')
win=tk.PhotoImage(file='img\win.png')
bg=tk.PhotoImage(file='img\g1.png')
canvas.pack(expand=True ,fill='both')
#-------------*USE KEY LEFT, RIGHT, UP, DOWN TO MOVE PACMAN*-------------------------#
root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)

#-----------------------------*DISPLAY WINDOWS*--------------------------------------#
root.mainloop()
