#!/bin/bash
set -x

# Base URL for the API
BASE_URL="http://localhost:5000"

# Function to test each endpoint
test_endpoints() {
    echo "Testing endpoint for viewing a comprehensive list of albums"
    curl "$BASE_URL/albums"

    echo -e "\nTesting endpoint for retrieving a list of all songs in a specified album using query parameters"
    curl "$BASE_URL/albums/songs?album_name=The%20Wall"

    echo -e "\nTesting endpoint for finding out the length of a specific song"
    curl "$BASE_URL/songs/length?song_name=Comfortably%20Numb"

    echo -e "\nTesting endpoint for accessing the full lyrics of a specific song"
    curl "$BASE_URL/songs/lyrics?song_name=Comfortably%20Numb"

    echo -e "\nTesting endpoint for discovering which album a particular song belongs to"
    curl "$BASE_URL/songs/album?song_name=Comfortably%20Numb"

    echo -e "\nTesting endpoint for searching for songs by name"
    curl "$BASE_URL/search/songs?name=pig"

    echo -e "\nTesting endpoint for searching for songs by lyrics"
    curl "$BASE_URL/search/songs/lyrics?lyrics=brick%20in%20the%20wall"

    echo -e "\nTesting endpoint shutdown server"
    curl -X POST "$BASE_URL/exit"
}

# Call the function to test all endpoints
test_endpoints