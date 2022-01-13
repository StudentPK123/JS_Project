from database.Database import *
from abc import abstractmethod


class AbstractGraph:
    @abstractmethod
    def get_nodes(self, city_index):
        pass

    @abstractmethod
    def get_index(self, city):
        pass

    @abstractmethod
    def get_city_by_index(self, city_index):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def debug_print(self):
        pass

    def find_connection(self, start, destination):
        start_index = self.get_index(start)
        destination_index = self.get_index(destination)

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
    def __init__(self):
        self.adjacency_list = []
        self.update()

    def get_index(self, city):
        return CITY_LIST.index(city)

    def get_city_by_index(self, city_index):
        return CITY_LIST[city_index]

    def get_nodes(self, city_index):
        return self.adjacency_list[city_index]

    def update(self):
        self.adjacency_list.clear()
        for start in CITY_LIST:
            self.adjacency_list.append([city_index for city_index in range(len(CITY_LIST)) if (start, self.get_city_by_index(city_index)) in RAILWAY_CONNECTIONS])

    def debug_print(self):
        for city_index in range(len(self.adjacency_list)):
            print(self.get_city_by_index(city_index) + " -> " + ",".join([ self.get_city_by_index(connection) for connection in self.adjacency_list[city_index]]))


class NeighborhoodMatrix(AbstractGraph):
    def __init__(self):
        self.matrix = []
        self.update()

    def is_connection(self, start, destination):
        return self.matrix[start * len(CITY_LIST) + destination]

    def update(self):
        self.matrix.clear()
        for start in CITY_LIST:
            for destination in CITY_LIST:
                self.matrix.append((start, destination) in RAILWAY_CONNECTIONS)

    def debug_print(self):
        max_column_len = 0
        for column in CITY_LIST:
            max_column_len = max(len(column),max_column_len)
        max_column_len = max_column_len + 1

        for i in range(max_column_len):
            print(' ', end='')

        for column in CITY_LIST:
            print(column, end=' ')
        print('')

        for start in range(len(CITY_LIST)):
            print(self.get_city_by_index(start), end='')
            for i in range(max_column_len - len(self.get_city_by_index(start))):
                print(' ', end='')
            for destination in range(len(CITY_LIST)):
                current_city_len = len(self.get_city_by_index(destination))
                is_connected = str(self.is_connection(start, destination))
                print(is_connected, end='')
                if current_city_len > len(is_connected):
                    for i in range(current_city_len - len(is_connected) + 1):
                        print(' ', end='')
            print('')

    def get_nodes(self, city_index):
        return [i for i in range(len(CITY_LIST)) if self.matrix[city_index * len(CITY_LIST) + i]]

    def get_index(self, city):
        return CITY_LIST.index(city)

    def get_city_by_index(self, city_index):
        return CITY_LIST[city_index]