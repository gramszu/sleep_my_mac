import subprocess
import time
import sys
import argparse
import tkinter as tk
from tkinter import messagebox

def sleep_mac(seconds):
    global running
    running = True
    for i in range(seconds, 0, -1):
        if not running:
            break
        label.config(text=f"Time to sleep: {i} sec(y).")
        root.update()
        time.sleep(1)

    if running:
        label.config(text="Sleep Mac")
        root.update()
        subprocess.run(["pmset", "sleepnow"])

def start_sleep():
    global running
    if not running:
        czas_sekundy = int(entry.get())
        running = True
        sleep_mac(czas_sekundy)

def stop_sleep():
    global running
    running = False
    label.config(text="")

def show_about():
    messagebox.showinfo("About", "Sleep Mac \nV1.0\nAutor: Robert Gramsz \nwww.megaelektronik.pl")

root = tk.Tk()
root.title("Sleep Mac")
root.geometry("300x250")

entry_label = tk.Label(root, text="Enter time [s]:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=10)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_sleep, bg="blue")
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_sleep)
stop_button.pack(pady=5)

about_button = tk.Button(root, text="About", command=show_about)
about_button.pack(pady=5)

label = tk.Label(root, text="")
label.pack(pady=10)

running = False

root.mainloop()
