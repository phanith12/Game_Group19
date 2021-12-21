import tkinter as tk
from random import randrange

window = tk.Tk()
window.geometry("600x600")
window.title("Hello PNC")
frame =tk.Frame()
canvas = tk.Canvas(frame)

index = 1
for row in range(1,6):
    for col in range(1,6):
        if index == col:
            canvas.create_oval(row*50,col*50,45+(row*50),45+(col*50), fill="red")
        else:
            canvas.create_oval(row*50,col*50,45+(row*50),45+(col*50), fill="blue")
    index +=1
canvas.pack(expand= True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()