import unittest

from UI.Windows import *
from graphs.Graphs import *

class TestSum(unittest.TestCase):
    # 1
    def test_connection_between_two_cities(self):
        find_graph = AdjacencyLists()
        self.assertEqual(len(find_graph.find_connection("Kraków", "Wrocław")),2)

    # 2
    def test_connections_between_two_cities_with_switches(self):
        find_graph = NeighborhoodMatrix()
        self.assertGreaterEqual(len(find_graph.find_connection("Kielce", "Kalisz")), 4)

    # 3
    def test_adding_direct_connection(self):
        find_graph = NeighborhoodMatrix()
        RAILWAY_CONNECTIONS.append(("Kielce", "Kalisz"))
        find_graph.update()
        self.assertEqual(len(find_graph.find_connection("Kielce", "Kalisz")), 2)

    # 4
    def test_deleting_direct_connections(self):
        find_graph = AdjacencyLists()
        RAILWAY_CONNECTIONS.remove(("Kraków", "Wrocław"))
        find_graph.update()
        self.assertGreaterEqual(len(find_graph.find_connection("Kraków", "Wrocław")), 3)

if __name__ == '__main__':
    unittest.main()