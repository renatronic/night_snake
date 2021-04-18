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
arabian = arabian.resize((width, height), Image.ANTIALIAS)
arabian_resized = ImageTk.PhotoImage(arabian)

balloon = Image.open('C:/Users/m64/Downloads/python/night_snake/img/balloon.jpeg')
balloon = balloon.resize((width, height), Image.ANTIALIAS)
balloon_resized = ImageTk.PhotoImage(balloon)

backgroundLabel = tk.Label(root, image = arabian_resized)
backgroundLabel.place(x = 0, y = 0)

root.mainloop()