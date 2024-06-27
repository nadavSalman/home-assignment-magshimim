import os

from disconfiguration_parser.albums import Album
from disconfiguration_parser.songs import Song


class DataLoader:
    def __init__(self, data_path=None):
        if data_path == None:
            current_script_path = os.path.abspath(__file__)
            self.data_path = data_path = f"{os.path.dirname(os.path.dirname(current_script_path))}/Pink_Floyd_DB.txt"
            print(f"Pink_Floyd_DB.txt full path : {self.data_path}")
        else:
            self.data_path = data_path
        self.albums:list[Album] = []
        self.sorted_songs_list:list[Song] = []
        
    def load_data(self):
                
        with open(self.data_path, 'r') as file:
            
            active_album:Album = None
            active_song:Song = None
            
            for line in file:
                line = line[:-1] # remove new line '\n'
                
                match line[0]:  
                    case "#":
                        line = line[1:]  # cut off '#'
                        # Album Parsing
                        albome_name, published_year = line.split('::')
                        self.albums.append(Album(
                            album_name=albome_name,
                            published_year=published_year
                        ))
                        active_album = self.albums[-1] # Point to the last album
                    case "*":
                        line = line[1:] # cut off '*'
                        # Song Parsing
                        song_name, singer, duration, first_line = line.split('::')
                        
                        if first_line == 'Instrumental':
                            active_song = Song(
                                song_name=song_name,
                                singer=singer,
                                duration=duration,
                                lines=[]
                            )
                        else:                   
                            active_song = Song(
                                song_name=song_name,
                                singer=singer,
                                duration=duration,
                                lines=[first_line]
                            )
                            
                        # Update song insied the album
                        active_album.add_song(active_song)
                        active_song = active_album.get_sorted_songs()[-1] # Point to the last song
                        
                    case _: # default - middle of the song
                        active_song.add_song_line(line)
    
    def get_albums(self) -> list[Album]:   
        return self.albums
    
    def get_sorted_songs_list(self) -> list[Song]:
        return self.sorted_songs_list
    
    def get_list_of_albums_names(self) -> list[str]:
        return [album.get_album_name() for album in self.albums]