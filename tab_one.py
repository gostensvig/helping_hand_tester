from tkinter import Frame, Label, Entry, Button
from file_handler import write_timestamp_to_file
from cli_handler import run_command


class Tab1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        lbl_1 = Label(self, text="Log Timestamp")
        lbl_1.pack()

        entry = Entry(self)
        entry.insert(0, "test")
        entry.pack()

        button = Button(
            self, text="Add", command=lambda: write_timestamp_to_file(entry.get())
        )
        button.pack()

        button = Button(
            self,
            text="Run command",
            command=lambda: run_command(entry.get()),
        )

        button.pack()
