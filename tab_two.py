from tkinter import Frame, Label, Entry, Button
from cli_handler import run_command


class Tab2(Frame):
    """
    Tab 2 : Test for now
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)

        lbl_1 = Label(self, text="Log Timestamp")
        lbl_1.pack()

        entry = Entry(self)
        entry.insert(0, "test")
        entry.pack()

        button = Button(
            self,
            text="Run command",
            command=lambda: run_command(entry.get()),
        )

        button.pack()
