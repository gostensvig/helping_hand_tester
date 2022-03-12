import tkinter as tk
from tkinter import Label, Button, Entry
from file_handler import write_timestamp_to_file


class Tab2(tk.Frame):
    """
    Tab 2 'Send (queue rsync)'
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        add_label = Label(self, text="Log-Timestamp to Send:")
        add_label.pack(fill="both")

        entry = Entry(self, width=25)
        entry.insert(0, "20xx-xx-xx-xx-xx-xx-xxx")
        entry.pack()

        button = Button(
            self, text="Add", command=lambda: write_timestamp_to_file(entry.get())
        )
        button.pack()

        queue_label = Label(self, text="Queued Timestamps:")
        queue_label.pack(fill="both")

        list_label = Label(self, text="Dis here")
        list_label.pack(fill="both")