import tkinter as tk
import threading
import random
import time

YELLOW = "#F1F7B5"
PINK = "#FD8A8A"
PURPLE = "#863A6F"
RED = "#FF1E00"
GREEN = "#285430"
BLACK = "#000000"

typing_samples = [
    "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.",
    "Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together.",
    "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.",
    "You'll find that education is just about the only thing lying around loose in this world, and it's about the only thing a fellow can have as much of as he's willing to haul away.",
    "We need women at all levels, including the top, to change the dynamic, reshape the conversation, to make sure women's voices are heard and heeded, not overlooked and ignored."
]

starting = False
speed_count = 0


def start(event):
    global starting

    if not starting:
        if event.keycode not in [16, 17, 18]:
            starting = True
            thread = threading.Thread(target=speed_check)
            thread.start()

    if not typing_text_label.cget("text").startswith(typing_entry.get()):
        typing_entry.config(fg=RED)
    else:
        typing_entry.config(fg=BLACK)

    if typing_entry.get() == typing_text_label.cget("text")[:-1]:
        starting = False
        typing_entry.config(fg=GREEN)


def speed_check():
    global starting, speed_count

    while starting:
        time.sleep(0.1)
        speed_count += 0.1
        cps = len(typing_entry.get()) / speed_count
        cpm = cps * 60
        wps = len(typing_entry.get().split()) / speed_count
        wpm = wps * 60
        speed_label.config(text=f"Speed:\n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")


def reset():
    global starting, speed_count

    starting = False
    speed_count = 0
    typing_text_label.config(text=random.choice(typing_samples))
    speed_label.config(text="Speed:\n 0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
    typing_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Welcome to the Typing Speed Test!")
window.minsize(width=700, height=500)
window.config(bg=YELLOW, padx=30, pady=65)

welcome_label = tk.Label(text="Please type as below in the box", fg=PINK, bg=YELLOW, font=("Arial", 20, "bold"))
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

typing_text_label = tk.Label(text=random.choice(typing_samples),
                             bg=YELLOW,
                             font=("Arial", 15, "normal"),
                             wraplength=650,
                             justify="center")
typing_text_label.grid(row=1, column=0, columnspan=2, pady=20)

typing_entry = tk.Entry(width=80, font=("Arial", 15, "normal"))
typing_entry.grid(row=2, column=0, columnspan=2, pady=20)
typing_entry.bind("<KeyPress>", func=start)

speed_label = tk.Label(text="", fg=PURPLE, bg=YELLOW, font=("Arial", 15, "bold"))
speed_label.grid(row=3, column=0, columnspan=2, pady=20)

reset_button = tk.Button(text="Reset", fg=PINK, bg=YELLOW, font=("Arial", 15, "bold"), command=reset)
reset_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
