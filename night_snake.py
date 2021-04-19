import tkinter as tk
import turtle
from PIL import ImageTk, Image
from pygame import mixer

root = tk.Tk()
root.title('NightSnake')
# root.iconbitmap('snake.ico')
root.state('zoomed')

def on_closing():
    mixer.music.stop()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', on_closing)

mixer.init()
mixer.music.load('sands_of_mystery.mp3')
mixer.music.play()

width = root.winfo_screenmmwidth()
height = root.winfo_screenmmheight()

arabian = Image.open('C:/Users/m64/Downloads/python/night_snake/img/arabian.jpeg')
arabian = arabian.resize((1920, 1080), Image.ANTIALIAS) # THE IMAGES ARE NOT BEING PROPERLY RESIZED
arabian_resized = ImageTk.PhotoImage(arabian)

balloon = Image.open('C:/Users/m64/Downloads/python/night_snake/img/balloon.jpeg')
balloon = balloon.resize((width, height), Image.ANTIALIAS)
balloon_resized = ImageTk.PhotoImage(balloon)

backgroundLabel = tk.Label(root, image = arabian_resized)
backgroundLabel.place(x = 0, y = 0)

# create a canvas
canvas = tk.Canvas(root, width = 600, height = 600)

# create a turtle screen
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor('#c2c2d6')

canvas.pack(pady = 10)

# create the snake head
head = turtle.RawTurtle(turtle_screen)
head.shape('triangle')
head.color('#cc0000')
head.goto(0,0)
head.direction = 'stop'
head.penup() # comment out to see what it looks like when the snake starts to move

root.mainloop()