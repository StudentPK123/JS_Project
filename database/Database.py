from exceptions.Exceptions import *

#list of cities with railway stations
CITY_LIST = [
    "Kraków",
    "Katowice",
    "Wrocław",
    "Białogard",
    "Ciechanów",
    "Białystok",
    "Giżycko",
    "Gniezno",
    "Poznań",
    "Kalisz",
    "Kielce",
    "Kołobrzeg"
]

#list of train connections between the various cities
RAILWAY_CONNECTIONS = [
    (0, 2),
    (0, 7),
    (7, 2),
    (2, 9),
    (9, 11),
    (11, 8),
    (7, 11),
    (11, 0),
    (10, 8),
    (8, 6),
    (6, 5),
    (5, 9)
]

class Database:
    def __init__(self, city_list, connections):
        self.city_list = []
        self.connections = []
        self.update_callbacks = []
        self.reload_callbacks = []
        self.reload(city_list.copy(), connections.copy())

    def reload(self, city_list, connections):
        self.city_list = city_list
        self.connections = connections
        for callback in self.reload_callbacks:
            callback()

    def get_city_name_by_id(self, id):
        return self.city_list[id]

    def add_update_callback(self, callback):
        self.update_callbacks.append(callback)

    def add_realod_callback(self, callback):
        self.reload_callbacks.append(callback)

    def get_city_id_by_name(self, city_name):
        return self.city_list.index(city_name)

    def has_connection(self, start_id, end_id):
        return (start_id, end_id) in self.connections

    def get_city_list(self):
        return self.city_list

    def get_connections(self):
        return self.connections

    def mange_connection(self, start_id, end_id, add):
        exists_connection = self.has_connection(start_id, end_id)
        if (exists_connection and add) or (not exists_connection and not add):
            raise RailwayConnectionError((self.get_city_name_by_id(start_id), self.get_city_name_by_id(end_id)),
                                         RailwayConnectionErrorType.EXISTS if add else RailwayConnectionErrorType.DO_NOT_EXISTS)
        self.connections.append((start_id, end_id)) if add else self.connections.remove((start_id, end_id))
        for callback in self.update_callbacks:
            callback(start_id, end_id, add)