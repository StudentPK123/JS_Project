import tkinter as tk

from tkinter import ttk

class MainWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System połączeń kolejowych")
        self.root.configure(bg='lightgray')

        tab_control = ttk.Notebook(self.root)

        tab_setting = ttk.Frame(tab_control)
        tab_search_connection = ttk.Frame(tab_control)

        tab_control.add(tab_setting, text='Ustawienia połączeń')
        tab_control.add(tab_search_connection, text='Wyszukiwanie połączeń')
        tab_control.pack(expand=1, fill="both")

        self.root.mainloop()