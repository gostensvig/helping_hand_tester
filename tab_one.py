from tkinter import Label, Button, Entry, Frame
from file_handler import write_timestamp_to_file


class Tab1(Frame):
    """
    Tab 1 'Send (queue rsync)'
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)

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
        # TODO Create a way to update the list_label to match the contents of timestamp_queue.txt
