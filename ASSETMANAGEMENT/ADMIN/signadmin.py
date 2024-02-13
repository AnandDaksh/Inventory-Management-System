import ADMINPG
import USERPG
import enginnerpage
from tkinter import *
from tkinter import messagebox

from connection import test_connection
import ttkbootstrap as ttk
from ttkbootstrap.style import Bootstyle

root = ttk.Window(themename="cyborg")
root.geometry("1220x720")
root.configure(bg="#b1d2f0")
# test_connection()

frame = Frame(root, bg="white", width="400", height="900")
frame.pack(pady=150, padx=20)

TEXT_IRCON = Label(frame, text="IRCON", height=5, width=40, bg="white", fg="black")
TEXT_IRCON.config(font=("ALGERIAN", 18))
TEXT_IRCON.pack()

b1 = ttk.Button(frame, text="ADMIN", command=ADMINPG.admin_button_clicked,bootstyle="danger-outline")
b1.pack(pady=10)

b2 = ttk.Button(frame, text="USER", command=USERPG.user_button_clicked,bootstyle="danger-outline")
b2.pack(pady=10)

b3 = ttk.Button(frame, text="ENGINEER",bootstyle="danger-outline",command=enginnerpage.engineer_button_clicked)
b3.pack(pady=10)

root.resizable(0, 0)
root.mainloop()
