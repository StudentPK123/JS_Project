import tkinter as tk

from tkinter import ttk

from Graphs.graphs import *

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

        label1 = tk.Label(tab_setting, text="Miejsce początkowe")
        label1.pack(padx=5, pady=5)

        self.start_combo = ttk.Combobox(tab_setting, values=CITY_LIST)
        self.start_combo.pack(padx=25, pady=5)

        label2 = tk.Label(tab_setting, text="Miejsce docelowe")
        label2.pack(padx=5, pady=5)

        self.destination_combo = ttk.Combobox(tab_setting, values=CITY_LIST)
        self.destination_combo.pack(padx=25, pady=5)

        #connect/disconnect button
        button1 = tk.Button(tab_setting, text="Połącz", command= lambda: self.manage_connection_button_handler(True))
        button1.pack(padx=5, pady=5)
        button2 = tk.Button(tab_setting, text="Rołącz", command= lambda: self.manage_connection_button_handler(False))
        button2.pack(padx=5, pady=5)

        #selecting a neighborhood type
        var = tk.IntVar()
        r1 = tk.Radiobutton(tab_setting, text="Macierz sąsiedztwa", variable=var, value=1,
                            command=lambda: self.update_graph(self.graph_neighborhood_matrix))
        r1.pack(anchor=tk.W)
        r1.select()

        r2 = tk.Radiobutton(tab_setting, text="Listy sąsiedztwa", variable=var, value=2,
                            command=lambda: self.update_graph(self.graph_adjacency_lists))
        r2.pack(anchor=tk.W)


        self.root.mainloop()