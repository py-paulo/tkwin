import random

import tkinter as tk

from tkinter import ttk


window_width = 600
window_height = 400


def get_random_position(last_position_x, last_position_y, size_x, size_y):
    x = random.randint(5, window_width - size_x)
    y = random.randint(5, window_height - size_y)

    while abs(last_position_x - x) < 100:
        x = random.randint(5, window_width - size_x)
    while abs(last_position_y - y) < 50:
        y = random.randint(5, window_height - size_x)

    return x, y


def return_hover(_):
    x, y = get_random_position(btn.winfo_x(), btn.winfo_y(), btn.winfo_width(), btn.winfo_height())
    btn.place(x=x, y=y)


root = tk.Tk()

root.title('Tk Window Demo')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.iconbitmap('./assets/skull.ico')

btn = ttk.Button()
btn.config(text='ClickMe', padding='3 3 3 3')
root.bind('<Enter>', return_hover)

btn.pack()

if __name__ == '__main__':
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()
