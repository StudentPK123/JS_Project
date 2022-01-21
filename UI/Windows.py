"""Moduł graficzny projektu."""

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from graphs.Graphs import *
from exceptions.Exceptions import *

def show_error_message_tk(error):
    """Wyświetlenie okienka z tytułem "Błąd" oraz treścią błędu"""
    tk.messagebox.showerror(title="Bład",
                            message="{}".format(error))

def show_showinfo_message_tk(info):
    """Wyświetlenie okienka z tytułem "Sukces" oraz treścią sukcesu"""
    tk.messagebox.showinfo(title="Sukces",
                            message="{}".format(info))

def show_error_message(error : RailwayConnectionError):
    """Wyświetlenie okienka z tytułem "Bład" oraz treścią statusu połączenia między miastami w zależności od parametru z jakim została przesłana wiadomość"""
    tk.messagebox.showerror(title="Bład",
                            message=" Połączenie {} -> {} {}!".format(error.connection[0], error.connection[1],
                                                                      "już istnieje" if error.error_type == RailwayConnectionErrorType.EXISTS else "nie istnieje"))

class MainWindow():
    """Klasa obsługująca główne okno programu."""

    def __init__(self):
        """Inicjalizuje dane okna programu."""
        self.root = tk.Tk()
        self.database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        self.database.add_update_callback(self.on_update_database_connection)
        self.database.add_realod_callback(self.on_reload_database)
        self.graph_neighborhood_matrix = NeighborhoodMatrix(self.database)
        self.graph_adjacency_lists = AdjacencyLists(self.database)
        self.current_graph = self.graph_neighborhood_matrix
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

        self.start_combo = ttk.Combobox(tab_setting, values=self.database.get_city_list())
        self.start_combo.pack(padx=25, pady=5)

        label2 = tk.Label(tab_setting, text="Miejsce docelowe")
        label2.pack(padx=5, pady=5)

        self.destination_combo = ttk.Combobox(tab_setting, values=self.database.get_city_list())
        self.destination_combo.pack(padx=25, pady=5)

        # przyciski służące do połączenia/rozłączenia danych węzłów kolejowych
        button1 = tk.Button(tab_setting, text="Połącz", command=lambda: self.manage_connection_button_handler(True))
        button1.pack(padx=5, pady=5)

        button2 = tk.Button(tab_setting, text="Rołącz", command=lambda: self.manage_connection_button_handler(False))
        button2.pack(padx=5, pady=5)

        #radiobutton służący do wyboru danego typu sąsiedztwa (macierz/lista)
        var = tk.IntVar()
        r1 = tk.Radiobutton(tab_setting, text="Macierz sąsiedztwa", variable=var, value=1,
                            command=lambda: self.update_graph(self.graph_neighborhood_matrix))
        r1.pack(anchor=tk.W)
        r1.select()

        r2 = tk.Radiobutton(tab_setting, text="Listy sąsiedztwa", variable=var, value=2,
                            command=lambda: self.update_graph(self.graph_adjacency_lists))
        r2.pack(anchor=tk.W)

        self.tv_connections = ttk.Treeview(tab_setting)
        self.tv_connections['columns'] = self.database.get_city_list()

        for city in self.database.get_city_list():
            self.tv_connections.column(city, anchor=tk.CENTER, width=70, stretch=0)
            self.tv_connections.heading(city, text=city, anchor=tk.CENTER)

        self.tv_connections.column('#0', width=95, anchor=tk.W, stretch=0)
        self.tv_connections.heading('#0', text='', anchor=tk.W)

        self.force_update_connections_tree_list()

        self.tv_connections.pack(padx=15, pady=15)

        self.user_serach_start_combo = ttk.Combobox(tab_search_connection, values=self.database.get_city_list())
        self.user_serach_start_combo.pack(padx=25, pady=5)

        self.user_serach_destination_combo = ttk.Combobox(tab_search_connection, values=self.database.get_city_list())
        self.user_serach_destination_combo.pack(padx=25, pady=5)

        button3 = tk.Button(tab_search_connection, text="Szukaj", command=self.find_connection_button_handler)
        button3.pack(padx=5, pady=5)

        self.connections_label = tk.Label(tab_search_connection, text="")
        self.connections_label.pack(padx=5, pady=5)

        self.root.mainloop()

    def on_reload_database(self):
        """Funkcja służąca do wywołania aktualizacji bazy połączeń"""
        self.force_update_connections_tree_list()

    def on_update_database_connection(self, start, end, add):
        """Funkcja służąca do ustawienia pozycji polączenia w danym wierszu macierzy."""
        old = [value for value in self.tv_connections.item(start, 'values')]
        old[end] = 'X' if add else ''
        self.tv_connections.item(start, values = old)

    def update_graph(self, graph):
        """Funkcja służąca do aktualizacji grafu"""
        self.current_graph = graph

    def force_update_connections_tree_list(self):
        """Funkcja służąca do aktualizacji/tworzenia bazy połączeń"""
        self.tv_connections.delete(*self.tv_connections.get_children()) #usuwanie elementów z Treeview
        i = 0
        for city in self.database.get_city_list():
            city_id = self.database.get_city_id_by_name(city)
            connection_values = []
            for connection_city in range(len(self.database.get_city_list())):
                connection_values.append("X" if self.database.has_connection(city_id, connection_city) else "")
            self.tv_connections.insert(parent='', index=i, iid=i, text=city, values=connection_values)
            i = i + 1


    def find_connection_button_handler(self):
        """Funkcja służąca do znalezienia połączenia pomiędzy dwoma punktami wybranymi przez użytkownika"""
        start = self.user_serach_start_combo.current()
        destination = self.user_serach_destination_combo.current()
        if start == -1 or destination == -1:
            show_error_message_tk("Aby wyszukać połączenie musisz wybrać miejsce początkowe oraz docelowe!")
        path = self.current_graph.find_connection(start, destination)
        if not path:
            show_error_message_tk("Niestety nie udało nam się znaleść połączenia!")
            return

        self.connections_label.config(text =  ", ".join(["{} -> {}".format(self.database.get_city_name_by_id(path[i - 1]), self.database.get_city_name_by_id(path[i])) for i in range(1, len(path)) ]))


    def manage_connection_button_handler(self, connect):
        """Funkcja odpowiedzialna za poprawne dodawanie i usuwanie połączeń między dwoma miastami"""
        start = self.start_combo.current()
        destination = self.destination_combo.current()

        if start == -1 or destination == -1:
            show_error_message_tk("Aby modyfikować połączenie musisz wybrać miejsce początkowe oraz docelowe!")
            return
        if start == destination:
            show_error_message_tk("Nie można modyfikować połączenia do tych samych miast!")
            return
        try:
            self.database.mange_connection(start, destination, connect)
            show_showinfo_message_tk(
                "Pomyślnie {} połączenie {}-{}".format("dodano" if connect else "usunięto", self.start_combo.get(),
                                                       self.destination_combo.get()))
        except RailwayConnectionError as error:
            show_error_message(error)