from tkinter import *
import time

# ---------------- WINDOW ----------------
root = Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.config(bg="black")
root.resizable(False, False)

# ---------------- CLOCK FUNCTION ----------------
def clock():

    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    time_label.after(1000, clock)

# ---------------- TITLE ----------------
title = Label(
    root,
    text="Digital Clock",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="cyan"
)
title.pack(pady=10)

# ---------------- TIME LABEL ----------------
time_label = Label(
    root,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="white"
)
time_label.pack(pady=20)

# ---------------- DATE LABEL ----------------
date_label = Label(
    root,
    font=("Arial", 16),
    bg="black",
    fg="lightgreen"
)
date_label.pack()

# ---------------- RUN CLOCK ----------------
clock()

# ---------------- MAIN LOOP ----------------
root.mainloop()