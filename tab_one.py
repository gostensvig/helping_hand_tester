from tkinter import Label, Button, Entry, Frame
from file_handler import write_timestamp_to_file


class Tab1(Frame):
    """
    Tab 1 'Send (queue rsync)'
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.timestamp_list = []

        self.add_label = Label(self, text="Log-Timestamp to Send:")
        self.add_label.pack(fill="both")

        self.entry = Entry(self, width=25)
        self.entry.insert(0, "20xx-xx-xx-xx-xx-xx-xxx")
        self.entry.pack()

        self.button = Button(
            self,
            text="Add",
            command=lambda: write_timestamp_to_file(self, self.entry.get()),
        )
        self.button.pack()

        self.queue_label = Label(self, text="Queued Timestamps:")
        self.queue_label.pack(fill="both")

        self.list_label = Label(self, text="Dis here")
        self.list_label.pack(fill="both")
        # TODO Create a way to update the list_label to match the contents of timestamp_queue.txt

    def update_list():
        print("Updating list_label")
