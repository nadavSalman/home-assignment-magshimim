import unittest
from disconfiguration_parser.parser import DataLoader as Data


class TestDisconfigurationParser(unittest.TestCase):
    
    def test_albums_names(self):
        data_loader = Data()
        print(data_loader.get_list_of_albums_names())
        self.assertEqual(len(data_loader.get_list_of_albums_names()),8)