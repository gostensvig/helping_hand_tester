import tkinter as tk


class Tab2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is page 2")
        label.pack(fill="both", expand=True, padx=20, pady=10)

        feedback_lbl = tk.Label(self)
        feedback_lbl.pack()
