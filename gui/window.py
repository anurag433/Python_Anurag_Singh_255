import tkinter as tk
import time

def utime():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, utime)

window=tk.Tk()
window.title("Digital Clock")
window.geometry("300x150")

label = tk.Label(window, font=("Helvetica", 48), fg="black")
label.pack()

utime()
window.mainloop()
