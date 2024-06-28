from flask import Blueprint, render_template, jsonify, request
from disconfiguration_parser.parser import DataLoader as Data
from disconfiguration_parser.parser import Song

pink_floyd_blueprint = Blueprint('album_song', __name__)

@pink_floyd_blueprint.route('/albums', methods=['GET'])
def view_albums():
    albums = []  
    return jsonify(albums)

@pink_floyd_blueprint.route('/albums/<album_name>/songs', methods=['GET'])
def album_songs(album_name):
    songs = []  
    return jsonify(songs)


@pink_floyd_blueprint.route('/songs/<song_name>/length', methods=['GET'])
def song_length(song_name):
 
    length = "3:45" 
    return jsonify({'song': song_name, 'length': length})


@pink_floyd_blueprint.route('/songs/<song_name>/lyrics', methods=['GET'])
def song_lyrics(song_name):

    lyrics = "Not just another brick in the wall" 
    return jsonify({'song': song_name, 'lyrics': lyrics})

@pink_floyd_blueprint.route('/songs/<song_name>/album', methods=['GET'])
def song_album(song_name):
   
    album = "The Wall" 
    return jsonify({'song': song_name, 'album': album})


@pink_floyd_blueprint.route('/search/songs', methods=['GET'])
def search_songs_by_name():
    name_query = request.args.get('name')
    songs = [] 
    return jsonify(songs)


@pink_floyd_blueprint.route('/search/songs', methods=['GET'])
def search_songs_by_lyrics():
    lyrics_query = request.args.get('lyrics')
    songs = []  
    return jsonify(songs)

@pink_floyd_blueprint.route('/exit', methods=['POST'])
def exit_app():
    response = {'message': 'JWT expired, new one generated'}
    return jsonify(response)