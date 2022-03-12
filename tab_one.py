import tkinter as tk
from file_handler import write_timestamp_to_file
from cli_handler import run_command


class Tab1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        lbl_1 = tk.Label(self, text="Log Timestamp")
        lbl_1.pack()

        entry = tk.Entry(self)
        entry.insert(0, "test")
        entry.pack()

        button = tk.Button(
            self, text="Add", command=lambda: write_timestamp_to_file(entry.get())
        )
        button.pack()

        button = tk.Button(
            self,
            text="Run command",
            command=lambda: run_command(entry.get()),
        )

        button.pack()