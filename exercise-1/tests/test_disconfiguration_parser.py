import unittest
from disconfiguration_parser.parser import DataLoader as Data

'''
     data_loader = Data()
     data_loader.load_data()



      1 Get the albums list     
     print(f"1. {data_loader.get_list_of_albums_names() = }")    


      2 Get list of songs by album 
     print(f"2. {data_loader.get_album_songs(album_name='Remember a Day') = }")


      3 Get song duration 
     print(f"3. {data_loader.get_song_duration(song_name='Set the Controls for the Heart of the Sun') = }")


      4 Get song words
     print(f"4. {data_loader.get_song_words('Set the Controls for the Heart of the Sun') =  }")


      5 Get Album bay song
     print(f"5. {data_loader.get_album_by_song('Set the Controls for the Heart of the Sun') = }")

      6 Search songs by name 
     print(f"6. {data_loader.search_songs_by_name('pig') = }")

      7 Search song by  
     print(f"7. {data_loader.get_songs_by_lirycs('bar') = }")
'''
class TestDisconfigurationParser(unittest.TestCase):
    
    def test_albums_names(self):
        data_loader = Data()
        print(data_loader.get_list_of_albums_names())
        self.assertListEqual(len(data_loader.get_list_of_albums_names()),8)