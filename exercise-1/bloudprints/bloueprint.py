from flask import Blueprint, jsonify, request
from disconfiguration_parser.parser import DataLoader as Data
import time
import os
import signal


def shutdown_server():
    if os.name == 'nt':
        # Windows-specific shutdown
        import ctypes
        ctypes.windll.kernel32.GenerateConsoleCtrlEvent(0, 0)
    else:
        # Unix-specific shutdown
        os.kill(os.getpid(), signal.SIGINT)

# Globals - need to be improved....
data_loader = Data()
data_loader.load_data()
pink_floyd_blueprint = Blueprint('album_song', __name__)

# 1
@pink_floyd_blueprint.route('/albums', methods=['GET'])
def view_albums():
    albums = data_loader.get_list_of_albums_names() 
    if albums != []:
        return jsonify(albums), 200
    else:
        return jsonify(albums), 400

# 2
@pink_floyd_blueprint.route('/albums/songs', methods=['GET'])
def album_songs():
    album_name = request.args.get('album_name')
    songs = data_loader.get_album_songs(album_name)
    return jsonify(songs)

# 3
@pink_floyd_blueprint.route('/songs/length', methods=['GET'])
def song_length():
    song_name = request.args.get('song_name')
    length = data_loader.get_song_duration(song_name)
    return jsonify({'song': song_name, 'length': length})

# 4
@pink_floyd_blueprint.route('/songs/lyrics', methods=['GET'])
def song_lyrics():
    song_name = request.args.get('song_name')
    lyrics = data_loader.get_song_words(song_name)
    return jsonify({'song': song_name, 'lyrics': lyrics})

# 5
@pink_floyd_blueprint.route('/songs/album', methods=['GET'])
def song_album():
    song_name = request.args.get('song_name')
    album = data_loader.get_album_by_song(song_name)
    return jsonify({'song': song_name, 'album': album})

# 6
@pink_floyd_blueprint.route('/search/songs', methods=['GET'])
def search_songs_by_name():
    search_input = request.args.get('name')
    songs = data_loader.search_songs_by_name(search_input)
    return jsonify(songs)

#7
@pink_floyd_blueprint.route('/search/songs/lyrics', methods=['GET'])
def search_songs_by_lyrics():
    lyrics_query = request.args.get('lyrics')
    songs = data_loader.get_songs_by_lirycs(search_input=lyrics_query)
    return jsonify(songs)

# 8
@pink_floyd_blueprint.route('/exit', methods=['POST'])
def exit_app():
    response = {'message': 'Shutting down server...'}
    time.sleep(5)  # Wait for 5 seconds
    shutdown_server()
    return jsonify(response)
