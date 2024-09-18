from PIL import ImageTk, Image
from tkmacosx import Button

from canvas import frame, root
from helpers import clear_screen
from json import load, dump


def display_products():
    clear_screen()
    display_stock()


def display_stock():
    with open("db/stock_info.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = Image.open(item_info["image"])
        resized_img = item_img.resize((100, 100))
        tk_img = ImageTk.PhotoImage(resized_img)
        images.append(tk_img)

        frame.create_text(x, y, text=item_name)
        frame.create_image(x, y + 100, image=tk_img)

        if item_info["quantity"] > 0:
            color = "green"
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                bg="green",
                fg="white",
                width=50,
                command=lambda x=item_name, y=info: buy_products(x, y)
            )

            frame.create_window(x, y + 220, window=item_button)

        else:
            color = "red"
            text = "Out of stock"

        frame.create_text(x, y + 180, text=text, fill=color)

        x += 200

        if x >= 650:
            y += 270
            x = 150


def buy_products(product_name, info):
    info[product_name]["quantity"] -= 1

    with open("db/stock_info.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []
