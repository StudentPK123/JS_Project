from database.Database import *
from abc import abstractmethod


class AbstractGraph:
    @abstractmethod
    def get_nodes(self, city_index):
        pass

    @abstractmethod
    def debug_print(self):
        pass

    def find_connection(self, start_index, destination_index):
        q = []
        path = [start_index]
        q.append(path.copy())

        while q:
            path = q.pop(0)
            last = path[-1]

            if last == destination_index:
                return path

            nodes = self.get_nodes(last)
            for neighbour in nodes:
                if neighbour in path:
                    continue
                new_path = path.copy()
                new_path.append(neighbour)
                q.append(new_path)
        return []


class AdjacencyLists(AbstractGraph):
    def __init__(self, database):
        self.adjacency_list = []
        self.database = database
        self.database.add_update_callback(self.on_update)
        self.database.add_realod_callback(self.on_reload)
        self.force_update()

    def get_nodes(self, city_index):
        return self.adjacency_list[city_index]

    def on_update(self, start, end, add):
        self.adjacency_list[start].append(end) if add else self.adjacency_list[start].remove(end)

    def on_reload(self):
        self.force_update()

    def force_update(self):
        self.adjacency_list.clear()
        city_list_len = len(self.database.get_city_list())
        for start in range(city_list_len):
            self.adjacency_list.append([city_index for city_index in range(city_list_len) if self.database.has_connection(start, city_index)])

    def debug_print(self):
        for city_index in range(len(self.adjacency_list)):
            print(self.database.get_city_name_by_id(city_index) + " -> " + ",".join([self.database.get_city_name_by_id(connection) for connection in self.adjacency_list[city_index]]))


class NeighborhoodMatrix(AbstractGraph):
    def __init__(self, database):
        self.matrix = []
        self.database = database
        self.database.add_update_callback(self.on_update)
        self.database.add_realod_callback(self.on_reload)
        self.city_len = len(self.database.get_city_list())
        self.force_update()

    def on_update(self, start, end, add):
        self.matrix[start * self.city_len + end] = True if add else False

    def on_reload(self):
        self.force_update()

    def is_connection(self, start, destination):
        return self.matrix[start * self.city_len + destination]

    def force_update(self):
        self.matrix.clear()
        for start in range(self.city_len):
            for destination in range(self.city_len):
                self.matrix.append(self.database.has_connection(start, destination))

    def debug_print(self):
        max_column_len = 0
        for column in self.database.get_city_list():
            max_column_len = max(len(column),max_column_len)
        max_column_len = max_column_len + 1

        for i in range(max_column_len):
            print(' ', end='')

        for column in self.database.get_city_list():
            print(column, end=' ')
        print('')

        for start in range(self.city_len):
            print(self.database.get_city_name_by_id(start), end='')
            for i in range(max_column_len - len(self.database.get_city_name_by_id(start))):
                print(' ', end='')
            for destination in range(self.city_len):
                current_city_len = len(self.database.get_city_name_by_id(destination))
                is_connected = str(self.is_connection(start, destination))
                print(is_connected, end='')
                if current_city_len > len(is_connected):
                    for i in range(current_city_len - len(is_connected) + 1):
                        print(' ', end='')

            print('')

    def get_nodes(self, city_index):
        return [i for i in range(self.city_len) if self.matrix[city_index * self.city_len + i]]
