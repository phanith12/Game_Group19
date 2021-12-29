import tkinter as tk
from tkinter import font
from tkinter.constants import X
from random import randint, randrange
root=tk.Tk()
root.geometry("640x700")
frame = tk.Frame()
frame.master.title("Killer Car")
canvas=tk.Canvas(frame)
import winsound
#-----------------------------*BLOCK IMAGE*----------------------------------#
car = tk.PhotoImage(file='img\pu1.png')
Scar_car=tk.PhotoImage(file='img\down1.png')
Scar_car1=tk.PhotoImage(file='img\down2.png')
gass=tk.PhotoImage(file='img\gasss.png')
ver=tk.PhotoImage(file='img\er.png')
win=tk.PhotoImage(file='img\win.png')
menu=tk.PhotoImage(file='img\Mbg.png')
bg=tk.PhotoImage(file='img\g1.png')
#-------------------------------*VARIABLE*-------------------------------#
#--------------------------*CREATE GRID OF GAME*-------------------------#
numberCoins = 0
notFinished=True
grid =[
        [2,0,3,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,1,0,0,0,0,2],   
    ]
#----------------------*NUMBER 0 IS NOTHING*-------------------------------#
#----------------------*NUMBER 1 IS PLAYER*--------------------------------#
#----------------------*NUMBER 2 IS WALE*----------------------------------#
#----------------------*NUMBER 3 IS SCAR CAR*------------------------------#
#----------------------*NUMBER 4 IS POINT*---------------------------------#


#----------------------*CREATE FUNCTION TO START GAME*(BUTTON)-------------#
def start():
    # randomPointRow()
    moveCar()
    moveGass()
    myButton.place_forget()  
    exit.place_forget() 

#----------------------*CREATE FUNCTION TO PUSH GAME*----------------------#
def Stop(event):
    global passed
    passed = True

#----------------------*CREATE FUNCTION TO DRAW GIRD*----------------------#
def displayGrid():
    canvas.delete('all')
    global Grid, notFinished ,myScore 
    myScore = 'SCORE: ' + str(numberCoins )
    canvas.create_image (330,350 ,image=bg)
    y1 = -285
    y2 = -210
    x1=5
    x2=75
    isTrue=True
    if isTrue and numberCoins< 700:
        for col in grid:
            for row in col:
                if row==0:
                    canvas.create_rectangle(x1,y1,x2,y2, outline='')
                elif row==1:
                    canvas.create_image((x2-35),y2-35,image=car)
                elif row==3:
                    canvas.create_image(x2-35,y2-35, image=Scar_car )
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
    else:
        gameOver()
    canvas.create_text(100, 50 , text=myScore, font=('consolas', 24, 'bold'), fill='#e0e0e0')

#----------------------*CREATE FUNCTION TO MOVE SCAR CAR*------------------#
def randomCar():
    numCol = randrange(1, 6)
    return numCol
numRow = 0
def moveCar():
    global numRow, Grid
    print(numRow)
    col = randomCar()
    grid[numRow][col] = 3
    canvas.delete("all  ")
    displayGrid()
    if numRow < len(grid)-1:
        numRow += 1
    else:
        numRow = 0
        return None
        
    canvas.after(200, moveCar())


#----------------------*CREATE FUNCTION TO MOVE POINT*---------------------#                
def moveGass():
    global Grid
    isHas = False
    for col in range(len(grid)-1):
        for row in range(len(grid[col])):
            if grid[col][row] == 4 and not isHas and grid[col+1][row] == 0 :
                grid[col][row] = 0
                grid[col+1][row] = 4
                isHas = True
            elif grid[col][row] == 1 and not isHas and col>5 and grid[col-1][row] != 0 and grid[col+1][row] == 4:
                grid[col][row] = 0
                grid[col+1][row] = 1
                countCoins()
    displayGrid()
    canvas.after(800,lambda:moveGass())
    
#----------------------*CREATE FUNCTION TO COUNT POINT*--------------------#
def countCoins():
    global numberCoins
    numberCoins+=700

#-----------------------------*CREATE BUTTON (EXIT AND START*--------------#
myButton = tk.Button(root, text="Start",command=start)
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

#---------------------*END GAME WITH RESULT LOST (GAME OVER) AND WIN*---------#
def gameOver():
    canvas.create_image(320,350 ,image=ver)
    canvas.create_text(300,400,text="GAME OVER !" ,font=("Pursia",25,"bold"))
    winsound.PlaySound("sound\gameover1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def gameWin():
    canvas.create_image(320,350 ,image=win)
    winsound.PlaySound("sound\win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)  

#------------------------*CREATE FUNTION TO CHECK MOVE_POSITION*--------------#
def movePosition(move):
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and row < len(Grid[col])-1 and Grid[col][row+1]!=2 and move== 'Right' : 
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row] = 0      
                Grid[col][row+1] = 1
                isHas =True 
            if Grid[col][row] == 1 and not isHas and row > 0 and Grid[col][row-1]!=2 and move == 'Left':
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row] = 0
                Grid[col][row-1] = 1
                isHas =True  
            if Grid[col][row] == 1 and not isHas and col < len(Grid)-1 and move == 'Down':
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row] = 0
                Grid[col+1][row] = 1
                isHas =True
            if Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] == 0 and Grid[col-1][row] != 4 and move=='Up':
                winsound.PlaySound("sound/theSound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
                Grid[col][row] = 0
                Grid[col-1][row] = 1
                isHas =True
            elif Grid[col][row] == 1 and not isHas and col>5 and Grid[col-1][row] != 0 and Grid[col-1][row] == 4 and Grid[col-1][row] != 3:
                Grid[col][row] = 0
                Grid[col-1][row] = 1
                countCoins()
            # elif Grid[col][row] == 1 and Grid[col-1][row] == 3 and not isHas:
            #     Grid[col][row] = 0
            #     Grid[col-1][row] = 1
            #     gameOver()
                
    displayGrid()

#-----------*CREATE BLOCK FUNTION TO MOVE (LEFT , RIGHT, UP , DOWN)*----------#
def moveRight(event):
    movePosition('Right')
def moveLeft(event):
    movePosition('Left')
def moveDown(event):
    movePosition('Down')
def moveUp(event):
    movePosition('Up')

#-----------------------------*CREATE KEY MOVE*------------------------------#
root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)
root.bind("<p>",Stop)
#----------------------------------------------------------------------------#
frame.pack(expand=True ,fill='both')
canvas.pack(expand=True ,fill='both')
root.mainloop()


#----------------------------------------------------------------*THANKS YOU SO MUCH*---------------------------------------------------------------------------#
