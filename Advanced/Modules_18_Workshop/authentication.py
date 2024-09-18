from tkinter import Entry
from tkmacosx import Button

from canvas import root, frame
from buying_page import display_products
from helpers import clear_screen, get_password_hash
from json import dump, loads


def get_users_data():
    info_data = []

    with open("db/users_information.txt", "r") as file:
        for line in file:
            info_data.append(loads(line))

        return info_data


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=90,
        height=40,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        bd=0,
        width=90,
        height=40,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 210, window=login_button)


def register():
    clear_screen()

    frame.create_text(100, 50, text="First Name:")
    frame.create_text(100, 100, text="Last Name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(230, 50, window=first_name_box)
    frame.create_window(230, 100, window=last_name_box)
    frame.create_window(230, 150, window=username_box)
    frame.create_window(230, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=80,
        height=40,
        command=registration
    )

    frame.create_window(315, 250, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get()
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", "a") as users_files:
            info_dict['Password'] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_files)
            users_files.write("\n")

            display_products()


def check_registration(info_dict):
    frame.delete("error")

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                200,
                300,
                text=f"{key} can't be empty!",
                fill="red",
                tags="error"
            )
            return False

    users_data = get_users_data()

    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
                200,
                300,
                text="Username is already taken!",
                tags="error"
            )
            return False

    return True


def login():
    clear_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password")

    frame.create_window(230, 50, window=username_box)
    frame.create_window(230, 100, window=password_box)

    frame.create_window(300, 150, window=login_button)


def logging():
    if check_loging():
        display_products()
    else:
        frame.create_text(
            200,
            200,
            text="Invalid Username or Password!",
            fill="red",
            tags="error"
        )



def check_loging():
    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user = user["Username"]
        current_password = user["Password"]

        if current_user == user_username and current_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get()
    ]

    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break
        else:
            login_button["state"] = "normal"


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")

login_button = Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    bd=0,
    command=logging
)

login_button["state"] = "disabled"
root.bind("<KeyRelease>", change_login_button_status)