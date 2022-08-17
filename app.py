import random

import tkinter as tk

from tkinter import ttk


def get_random_position(size_box_x=0, size_box_y=0):
    x = random.randint(5, 600 - size_box_x)
    y = random.randint(5, 400 - size_box_y)
    return x, y


def callback_function(args):
    print('Button Clicked!', args)


def return_pressed(event):
    print('Return key pressed.', event)


def return_hover(event):
    x, y = get_random_position(size_box_x=btn.winfo_width(), size_box_y=btn.winfo_height())
    btn.place(x=x, y=y)
    print('Hover button', event)


root = tk.Tk()

root.title('Tk Window Demo')

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.iconbitmap('./assets/skull.ico')

btn = ttk.Button()
btn.config(text='ClickMe', command=lambda: callback_function(btn.winfo_screenheight()))
root.bind('<Return>', return_pressed)
root.bind('<Enter>', return_hover, add='+')

btn.pack()

if __name__ == '__main__':
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()
