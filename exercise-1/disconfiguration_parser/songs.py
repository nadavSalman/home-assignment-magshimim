class Song:
    def __init__(self, song_name: str, singer: str, duration: str, song_lines: list[str]) -> None:
        self.song_name = song_name
        self.singer = singer
        self.duration = duration
        self.song_lines = song_lines

    def get_song_name(self) -> str:
        return self.song_name

    def set_song_name(self, song_name: str) -> None:
        self.song_name = song_name

    def get_singer(self) -> str:
        return self.singer

    def set_singer(self, singer: str) -> None:
        self.singer = singer

    def get_duration(self) -> str:
        return self.duration

    def set_duration(self, duration: str) -> None:
        self.duration = duration

    def get_song_lines(self) -> list[str]:
        return self.song_lines

    def set_song_lines(self, song_lines: list[str]) -> None:
        self.song_lines = song_lines
        
    def add_song_line(self, song_line:str) -> None:
        self.song_lines.append(song_line)