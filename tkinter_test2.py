import tkinter as tk
import re

from PIL import Image, ImageTk

from tkinter import Canvas


def validate_email():
    email = input_field.get()
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-z0-9]+[.][a-z.]{2,6}$'

    canvas.delete('validation_text')
    if re.match(email_pattern, email):
        valid_label = canvas.create_text(100,300, text='Valid Email!', fill='green', font='Arial 20 bold', tags='validation_text')
    else:
        invalid_label = canvas.create_text(100,300, text='Invalid Email!!!', fill='red', font='Arial 20 bold', tags='validation_text')


window = tk.Tk()
window.title("Email Validator")
window.geometry("500x550")

bg_image = Image.open('blue-burst.png')
bg_image = ImageTk.PhotoImage(bg_image)


canvas = Canvas(window, width=500, height=500,)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=bg_image, anchor='nw')
canvas.create_text(235, 80, text="Check Email", fill='dark blue', font='Arial 20 bold')

validation_button = tk.Button(window, text='Validate', height=1, command=validate_email, bg='systemTransparent')
validation_button_canvas = canvas.create_window(348, 100, anchor='nw', window=validation_button)

input_field = tk.Entry(window, width=23)
input_field_canvas = canvas.create_window(130, 100, anchor='nw', window=input_field)


window.mainloop()


