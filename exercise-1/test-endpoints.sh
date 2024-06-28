#!/bin/bash

# Base URL for the API
BASE_URL="http://localhost:5000"

# Function to test each endpoint
test_endpoints() {
    echo "Testing endpoint for viewing a comprehensive list of albums"
    curl "$BASE_URL/albums"

    echo -e "\nTesting endpoint for retrieving a list of all songs in a specified album"
    curl "$BASE_URL/albums/Thriller/songs"

    echo -e "\nTesting endpoint for finding out the length of a specific song"
    curl "$BASE_URL/songs/BillieJean/length"

    echo -e "\nTesting endpoint for accessing the full lyrics of a specific song"
    curl "$BASE_URL/songs/BillieJean/lyrics"

    echo -e "\nTesting endpoint for discovering which album a particular song belongs to"
    curl "$BASE_URL/songs/BillieJean/album"

    echo -e "\nTesting endpoint for searching for songs by name"
    curl "$BASE_URL/search/songs?name=Billie"

    echo -e "\nTesting endpoint for searching for songs by lyrics"
    curl "$BASE_URL/search/songs?lyrics=moonwalk"

    echo -e "\nTesting endpoint to exit (JWT will be expired and a new one will be generated)"
    curl -X POST "$BASE_URL/exit"
}

# Call the function to test all endpoints
test_endpoints