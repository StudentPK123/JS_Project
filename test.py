import unittest
from graphs.Graphs import *

class TestRailwayConnections(unittest.TestCase):
    def helper_tester_b(self, adjacency_list):
        database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        graph = AdjacencyLists(database) if adjacency_list else NeighborhoodMatrix(database)
        self.assertGreaterEqual(len(graph.find_connection(database.get_city_id_by_name('Kielce'), database.get_city_id_by_name('Kalisz'))), 4)

    def helper_tester_c(self, adjacency_list):
        database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        graph = AdjacencyLists(database) if adjacency_list else NeighborhoodMatrix(database)
        start = database.get_city_id_by_name('Kielce')
        end = database.get_city_id_by_name('Kalisz')
        database.mange_connection(start, end, True)
        self.assertEqual(len(graph.find_connection(start, end)), 2)

    #1
    def test_connection_between_two_cities(self):
        database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        graph = AdjacencyLists(database)
        self.assertEqual(len(graph.find_connection(database.get_city_id_by_name('Kraków'), database.get_city_id_by_name('Wrocław'))), 2)

    #2
    def test_connections_between_two_cities_with_switches(self):
        self.helper_tester_b(True)

    #3
    def test_connection_between_two_cities_after_add(self):
        self.helper_tester_c(True)

    #4
    def test_connection_between_two_cities_after_remove(self):
        database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        graph = AdjacencyLists(database)
        start = database.get_city_id_by_name('Kraków')
        end = database.get_city_id_by_name('Wrocław')
        database.mange_connection(start, end, False)
        self.assertGreaterEqual(len(graph.find_connection(start, end)), 3)

    #5
    def test_delete_all_connections(self):
        database = Database(CITY_LIST, RAILWAY_CONNECTIONS)
        graph = AdjacencyLists(database)
        dest = database.get_city_id_by_name('Wrocław')
        remove_list = [ connection for connection in database.get_connections() if connection[1] == dest]
        for connection in remove_list:
            database.mange_connection(connection[0], connection[1], False)
        for start in range(len(database.get_city_list())):
            if start == dest:
                continue
            self.assertEqual(len(graph.find_connection(start, dest)), 0)

    #6
    def test_connections_between_two_cities_with_switches_second_graph(self):
        self.helper_tester_b(False)

    #7
    def test_connection_between_two_cities_after_add_second_graph(self):
        self.helper_tester_c(False)

if __name__ == '__main__':
    unittest.main()