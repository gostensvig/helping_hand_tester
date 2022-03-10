import tkinter as tk
from tkinter import Label, ttk
import os

root = tk.Tk()
root.title("Helping Hand Tester")
root.minsize(200, 200)

# Creating tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True)
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)
notebook.add(frame1, text="run regression")
notebook.add(frame2, text="send (rsync)")


def run_command(my_command, output_lbl):
    split_cmd = my_command.split(" ")
    print(my_command)
    print(split_cmd)
    os.system(f'gnome-terminal -- bash -c "{my_command}; exec bash"')
    output_lbl.configure(text="Command was run")


lbl_1 = ttk.Label(frame1, text="Log Timestamp")
lbl_1.pack()

# Enty
entry = ttk.Entry(frame1)
entry.insert(0, "test")
entry.pack()

# Button
button = ttk.Button(
    frame1, text="Click me!", command=lambda: run_command(entry.get(), lbl_2)
)

lbl_2 = Label()
lbl_2.pack()

button.pack()

root.mainloop()