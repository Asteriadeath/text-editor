import tkinter as tk
from tkinter import scrolledtext

def save_file():
    """Saves the current text to a file."""
    try:
        with open(save_path.get(), "w") as f:
            f.write(text_area.get("1.0", tk.END))
        status_label.config(text="File saved successfully!")
    except FileNotFoundError:
        status_label.config(text="Invalid file path!")

def open_file():
    """Opens a file and displays its contents."""
    try:
        with open(open_path.get(), "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())
        status_label.config(text="File opened successfully!")
    except FileNotFoundError:
        status_label.config(text="File not found!")

window = tk.Tk()
window.title("Simple Text Editor")

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

frame = tk.Frame(window)
frame.pack()

open_button = tk.Button(frame, text="Open", command=open_file)
open_button.pack(side=tk.LEFT)

save_button = tk.Button(frame, text="Save", command=save_file)
save_button.pack(side=tk.LEFT)

open_path = tk.Entry(frame)
open_path.pack(side=tk.LEFT)

save_path = tk.Entry(frame)
save_path.pack(side=tk.LEFT)

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()