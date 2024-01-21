from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import sqlite3

### Database ###
conn = sqlite3.connect('./sqlite.db');
if conn: 
    print("Connected to database");
cur = conn.cursor();
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT)");


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("605x404")
window.configure(bg = "#FFFFFF")
window.title("Login form")


### Functions ###

def on_button_click() :
    print("button_1 clicked");
    email = entry_1.get();
    password = entry_2.get();
    if email == "" or password == "" :
        print("Please fill all fields");
        messagebox.showinfo("Error", "Please fill all fields");
        return;

    elif not email.endswith("@gmail.com") :
        print("Please enter a valid email");
        messagebox.showinfo("Error", "Please enter a valid email");
        return;

    elif len(password) < 8 :
        print("Password must be at least 8 characters");
        messagebox.showinfo("Error", "Password must be at least 8 characters");
        return;

    

    print(email);
    print(password);
    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password));
    conn.commit();
    messagebox.showinfo("Success", "Data inserted");
    print("Data inserted");
    entry_1.delete(0, 'end');
    entry_2.delete(0, 'end');

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 404,
    width = 605,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    298.0,
    404.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    280.0,
    404.0,
    fill="#9199E2",
    outline="")

canvas.create_rectangle(
    326.0,
    168.0,
    575.0,
    211.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    450.5,
    187.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=345.0,
    y=172.0,
    width=211.0,
    height=28.0
)



canvas.create_rectangle(
    330.0,
    249.0,
    571.0,
    298.0,
    fill="#FFFFFF",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    449.5,
    271.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=344.0,
    y=256.0,
    width=211.0,
    height=28.0
)


canvas.create_text(
    302.0,
    24.0,
    anchor="nw",
    text="Create an account",
    fill="#000000",
    font=("LexendDeca Bold", 24 * -1)
)

canvas.create_text(
    316.0,
    61.0,
    anchor="nw",
    text="Join our network and be ready to find special offers.",
    fill="#000000",
    font=("LexendDeca ExtraLight", 11 * -1)
)

canvas.create_text(
    336.0,
    143.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("LexendDeca ExtraLight", 16 * -1)
)

canvas.create_text(
    336.0,
    227.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("LexendDeca ExtraLight", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_click,
    relief="flat"
)
button_1.place(
    x=473.0,
    y=337.0,
    width=98.0,
    height=40.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    152.0,
    203.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
