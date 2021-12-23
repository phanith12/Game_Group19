import tkinter as tk
from tkinter.constants import X
root=tk.Tk()
import random
root.geometry("700x700")
frame = tk.Frame()
frame.master.title("GUI")
canvas=tk.Canvas(frame)
car = tk.PhotoImage(file='img\pu1.png')
Scar_car=tk.PhotoImage(file='img\down1.png')
gass=tk.PhotoImage(file='img\gasss.png')
bg=tk.PhotoImage(file='img\g1.png')
#====menu and background======

Grid =[
        [2,0,0,0,0,0,0,0,2],
        [2,0,3,0,4,0,0,0,2],
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
    canvas.create_image (370,300 ,image=bg)
    global Grid
    y1 = 0
    y2 = 0
    x1=0
    x2=0
    for col in Grid:
        for row in col:
            if row==0:
                canvas.create_rectangle(x1,y1,x2,y2,outline='' )
            elif row==1:
                canvas.create_image((x2-40),y2-40,image=car)
            elif row==3:
                canvas.create_image((x2-40),y2-40,image=Scar_car)
            elif row == 4:
                canvas.create_image((x2-40),y2-40,image=gass)
            x1=x2
            x2 += 80
        x1 =80
        x2=80
        y1 = y2
        y2 += 80
displaygrid()

#=======care_random===================
def moveCar():
    global Grid
    isHas = False
    for col in range(len(Grid)-1):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 3 and not isHas :
                Grid[col][row] = 0
                Grid[col+1][row] = 3
                
                if Grid[col][row]== [col-1]:
                    canvas.delete('all')
                isHas = True
    displaygrid()
  
    canvas.after(1000,lambda:moveCar())
moveCar()

#========redom_gass===================
def move_gass():
    global Grid
    isHas = False
    for col in range(len(Grid)-1):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 4 and not isHas :
                Grid[col][row] = 0
                Grid[col+1][row] = 4
                isHas = True
    displaygrid()
    canvas.after(800,lambda:move_gass())
move_gass()
#============ move_care to right=======
def move_right(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and row < len(Grid[col])-1 and Grid[col][row+1]!=2:
                Grid[col][row] = 0
                Grid[col][row+1] = 1
                isHas =True
    
    
    displaygrid() 
root.bind("<Right>", move_right)

#============ move_care to left=======
def move_left(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and row > 0 and Grid[col][row-1]!=2:
                Grid[col][row] = 0
                Grid[col][row-1] = 1
                isHas =True
    
    displaygrid() 
root.bind("<Left>", move_left)
#============ move_care to down=======
def move_down(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and col < len(Grid)-1:
                Grid[col][row] = 0
                Grid[col+1][row] = 1
                isHas =True
    
    displaygrid()
root.bind("<Down>", move_down)

#============ move_care to down=======
def move_up(event):
    global Grid
    isHas = False
    for col in range(len(Grid)):
        for row in range(len(Grid[col])):
            if Grid[col][row] == 1 and not isHas and col>5:
                Grid[col][row] = 0
                Grid[col-1][row] = 1
                isHas =True
    
    displaygrid()
root.bind("<Up>", move_up)

frame.pack(expand=True ,fill='both')
canvas.pack(expand=True ,fill='both')
root.mainloop()


























