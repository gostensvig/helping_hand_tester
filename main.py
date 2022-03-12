import tkinter as tk
from tkinter import ttk
from tab_one import Tab1
from tab_two import Tab2


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        page1 = Tab1(self.notebook)
        page2 = Tab2(self.notebook)
        self.notebook.add(page1, text="Run Regression")
        self.notebook.add(page2, text="Send (queue rsync)")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Helping Hand Tester")
    root.minsize(300, 300)
    notebook = Example(root).pack(fill="both", expand=True)
    root.mainloop()
