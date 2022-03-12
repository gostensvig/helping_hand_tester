from tkinter import Label, Button, Entry, Frame, StringVar
from file_handler import read_timestamps_from_file, write_timestamp_to_file


class Tab1(Frame):
    """
    Tab 1 'Send (queue rsync)'
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.list_string_var = StringVar()
        self.placeholder_entry = StringVar()
        self.placeholder_entry.set("20xx-xx-xx-xx-xx-xx-xxx")

        self.add_label = Label(self, text="Log-Timestamp to Send:")
        self.add_label.pack(fill="both")

        self.entry = Entry(self, width=25, textvariable=self.placeholder_entry)
        self.entry.pack()

        self.button = Button(
            self,
            text="Add",
            command=self.queue_timestamp,
        )
        self.button.pack()

        self.queue_label = Label(self, text="Queued Timestamps:")
        self.queue_label.pack(fill="both")

        self.list_label = Label(self, textvariable=self.list_string_var)
        self.list_label.pack(fill="both")

    def queue_timestamp(self):
        write_timestamp_to_file(self.entry.get())
        timestamp_list = read_timestamps_from_file()
        txt = "".join(timestamp_list)
        self.list_string_var.set(txt)
