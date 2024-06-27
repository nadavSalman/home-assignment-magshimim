from disconfiguration_parser.parser import DataLoader as Data
from disconfiguration_parser.parser import Song


def main():
    data_loader = Data()
    data_loader.load_data()
    
    
    
    print(f"{data_loader.albums[-1].get_album_name() = }")
    for song in data_loader.albums[-1].get_sorted_songs():
        print(song.get_song_name())
    # print(f"{data_loader.albums[-1].get_sorted_songs() = }")
    

if __name__ == '__main__':
    main()