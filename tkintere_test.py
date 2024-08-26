import tkinter as tk
import re

from tkinter import Canvas


def validate_email():
    email = input_field.get()
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-z0-9]+[.][a-z.]{2,6}$'

    invalid_label.place_forget()
    valid_label.place_forget()
    if re.match(email_pattern, email):
        valid_label.place(x=200, y=200)
    else:
        invalid_label.place(x=130, y=125)


window = tk.Tk()
window.title("Email Validator")
window.geometry("500x250")

input_field = tk.Entry(window, width=23)
input_field.place(x=80, y=80)

validation_button = tk.Button(window, text='Validate',height=1, command=validate_email)
validation_button.place(x=300, y=79)

invalid_label = tk.Label(window, text="Invalid email!", font='Arial 20 bold', fg='red')
valid_label = tk.Label(window, text="Valid Email!", font='Arial 20 bold',fg='green')

canvas = Canvas(window, width=500, height=70)
canvas.create_text(200, 60, text="Check Email", fill='black', font='Arial 20 bold')
canvas.pack()

window.mainloop()

