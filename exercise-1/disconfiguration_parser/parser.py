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
        self.albums_dict:dict = {}
        
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
                        albome_name = albome_name.lower()
                        self.albums.append(Album(
                            album_name=albome_name,
                            published_year=published_year
                        ))
                        active_album = self.albums[-1] # Point to the last album
                        self.albums_dict[active_album.get_album_name()] = {}

                    case "*":
                        line = line[1:] # cut off '*'
                        # Song Parsing
                        song_name, singer, duration, first_line = line.split('::')
                        song_name = song_name.lower()
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
                        active_song = active_album.get_songs()[-1] # Point to the last song
                        self.albums_dict[active_album.get_album_name()][active_song.get_song_name()] = active_album.get_songs()[-1]
                        
                    case _: # default - middle of the song
                        active_song.add_song_line(line)
    
    def get_albums(self) -> list[Album]:   
        return self.albums
    
    def get_sorted_songs_list(self) -> list[Song]:
        return self.sorted_songs_list
    
    def get_list_of_albums_names(self) -> list[str]:
        return [album.get_album_name() for album in self.albums]
    
    def get_album_songs(self,album_name:str):
        album_name = album_name.lower()
        for album in self.albums:
            if album.get_album_name() == album_name:
                # print(f"{[s.get_song_name() for s in album.get_songs()] = }")
                return [song.get_song_name() for song in album.get_songs()]
        return []
    
    def get_song_duration(self,song_name):
        song_name = song_name.lower()
        for album in self.albums:
            if song_name in self.get_album_songs(album.get_album_name()):
                target_song = self.albums_dict[album.get_album_name()][song_name]
                return target_song.get_duration()
        return None

    def get_song_words(self,song_name):
        song_name = song_name.lower()
        for album in self.get_albums():
            if song_name in self.get_album_songs(album.get_album_name()):
                target_song = self.albums_dict[album.get_album_name()][song_name]
                return target_song.get_lines()
            
    def get_album_by_song(self,song_name):
        song_name = song_name.lower()
        for album in self.get_albums():
            if song_name in self.get_album_songs(album.get_album_name()):
                return album.get_album_name()
        return None

    def search_songs_by_name(self,search_input):
        search_input = search_input.lower()
        agrigate_songs_result = []
        for album in self.albums:
            agrigate_songs_result += [song_name for song_name in self.get_album_songs(album.get_album_name()) if search_input in song_name]
        return agrigate_songs_result

    def get_songs_by_lirycs(self,search_input):
        agrigate_songs_result = []
        search_input = search_input.lower()
        for album in self.albums:
            for song in album.get_songs():
                for line in song.get_lines():
                    if search_input in line and song.get_song_name() not in agrigate_songs_result :
                        agrigate_songs_result.append(song.get_song_name())
                  
        return agrigate_songs_result