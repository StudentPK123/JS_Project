import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from Graphs.graphs import *
from Exceptions.exceptions import *

def show_error_message_tk(error):
    tk.messagebox.showerror(title="Bład",
                            message="{}".format(error))

def show_showinfo_message_tk(info):
    tk.messagebox.showinfo(title="Sukces",
                            message="{}".format(info))

def show_error_message(error : RailwayConnectionError):
    tk.messagebox.showerror(title="Bład",
                            message=" Połączenie {} -> {} {}!".format(error.connection[0], error.connection[1],
                                                                      "już istnieje" if error.error_type == RailwayConnectionErrorType.EXISTS else "nie istnieje"))

class MainWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.graph_neighborhood_matrix = NeighborhoodMatrix()
        self.graph_adjacency_lists = AdjacencyLists()
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

        self.start_combo = ttk.Combobox(tab_setting, values=CITY_LIST)
        self.start_combo.pack(padx=25, pady=5)

        label2 = tk.Label(tab_setting, text="Miejsce docelowe")
        label2.pack(padx=5, pady=5)

        self.destination_combo = ttk.Combobox(tab_setting, values=CITY_LIST)
        self.destination_combo.pack(padx=25, pady=5)

        #connect/disconnect button
        button1 = tk.Button(tab_setting, text="Połącz", command=lambda: self.manage_connection_button_handler(True))
        button1.pack(padx=5, pady=5)
        button2 = tk.Button(tab_setting, text="Rołącz", command=lambda: self.manage_connection_button_handler(False))
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

        self.tv_connections = ttk.Treeview(tab_setting)
        self.tv_connections['columns'] = CITY_LIST

        for city in CITY_LIST:
            self.tv_connections.column(city, anchor=tk.CENTER, width=70)
            self.tv_connections.heading(city, text=city, anchor=tk.CENTER)

        self.tv_connections.column('#0', width=95, anchor=tk.W)
        self.tv_connections.heading('#0', text='', anchor=tk.W)

        self.update_connections_tree_list()

        self.tv_connections.pack(padx=15, pady=15)

        self.user_serach_start_combo = ttk.Combobox(tab_search_connection, values=CITY_LIST)
        self.user_serach_start_combo.pack(padx=25, pady=5)

        self.user_serach_destination_combo = ttk.Combobox(tab_search_connection, values=CITY_LIST)
        self.user_serach_destination_combo.pack(padx=25, pady=5)

        button3 = tk.Button(tab_search_connection, text="Szukaj", command=self.find_connection_button_handler)
        button3.pack(padx=5, pady=5)

        self.connections_label = tk.Label(tab_search_connection, text="")
        self.connections_label.pack(padx=5, pady=5)

        self.root.mainloop()

    def update_graph(self, graph):
        graph.update()
        self.current_graph = graph

    def update_connections_tree_list(self):
        self.tv_connections.delete(*self.tv_connections.get_children()) #cleaning treeview
        i = 0
        for city in CITY_LIST:
            connection_values = []
            for connectionCity in CITY_LIST:
                connection_values.append("X" if (city, connectionCity) in RAILWAY_CONNECTIONS else "")
            self.tv_connections.insert(parent='', index=i, iid=i, text=city, values=connection_values)
            i = i + 1

    def find_connection_button_handler(self):
        start = self.user_serach_start_combo.get().strip()
        destination = self.user_serach_destination_combo.get().strip()

        if not start or not destination:
            show_error_message_tk("Aby wyszukać połączenie musisz wybrać miejsce początkowe oraz docelowe!")
        path = self.current_graph.find_connection(start, destination)
        if not path:
            show_error_message_tk("Niestety nie udało nam się znaleść połączenia!")
            return

        self.connections_label.config(text=", ".join(["{} -> {}".format(
            self.current_graph.get_city_by_index(path[i - 1]), self.current_graph.get_city_by_index(path[i])) for i in
                                                      range(1, len(path))]))

    def manage_connection_button_handler(self, connect):
        start = self.start_combo.get().strip()
        destination = self.destination_combo.get().strip()

        if not start or not destination:
            show_error_message_tk("Aby modyfikować połączenie musisz wybrać miejsce początkowe oraz docelowe!")
            return
        if start == destination:
            show_error_message_tk("Nie można modyfikować połączenia do tych samych miast!")
            return
        connection = (start, destination)

        try:
            exists_connection = connection in RAILWAY_CONNECTIONS
            if (exists_connection and connect) or (not exists_connection and not connect):
                raise RailwayConnectionError(connection,
                                             RailwayConnectionErrorType.EXISTS if connect else RailwayConnectionErrorType.DO_NOT_EXISTS)
            RAILWAY_CONNECTIONS.append(connection) if connect else RAILWAY_CONNECTIONS.remove(connection)
            show_showinfo_message_tk("Pomyślnie {} połączenie {}-{}".format("dodano" if connect else "usunięto",
                                                                                  start, destination))
            self.update_connections_tree_list()
            self.current_graph.update()

        except RailwayConnectionError as error:
            show_error_message(error)
