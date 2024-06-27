from disconfiguration_parser.songs import Song

class Album:
    def __init__(self, album_name: str, published_year: str):
        self.album_name = album_name
        self.published_year = published_year
        self.sorted_songs = [] # songs are sorted A-Z by the song name .

    def get_album_name(self) -> str:
        return self.album_name

    def set_album_name(self, album_name: str):
        self.album_name = album_name

    def get_published_year(self) -> str:
        return self.published_year

    def set_published_year(self, published_year: str):
        self.published_year = published_year

    def get_sorted_songs(self) -> list:
        return self.sorted_songs

    def set_sorted_songs(self, sorted_songs: list):
        self.sorted_songs = sorted_songs
        
    def add_song(self, song:Song):
        self.sorted_songs.append(song)