# Home assignment `Magshimim`
<br/>
<br/>
<br/>
<br/>


# Exercise - 1

![Alt text](images/exercise-1.png)


## Pink Floyd Song Serach Application

This document outlines the features available in the Pink Floyd Song Serach application.

1. **List of Albums**
   - Users can view a list of Pink Floyd albums.

2. **List of Songs in an Album**
   - By entering the name of an album, users can retrieve a list of all songs contained within that album.

3. **Get the Length of a Song**
   - Users can find out the length of a specific song by typing its name.

4. **Get the Lyrics of a Song**
   - By typing the name of a song, users can access its full lyrics.

5. **In Which Album is the Song**
   - Users can discover which album a particular song belongs to by entering the song's name.

6. **Search for a Song by Name**
   - Users can search for songs by typing a word or phrase. The search returns all song names that include the typed word, ignoring case sensitivity.

7. **Search for a Song by Lyrics**
   - Similar to searching by name, users can type a word or phrase to find all songs whose lyrics contain the specified word, regardless of case sensitivity.

8. **Exit**
   - Users can exit the application.


Lunch the server localy : ` exercise-1/bootstrap.sh `

REST Implementation 

| Feature Number | Description | HTTP Method | Route Endpoint |
|----------------|-------------|-------------|----------------|
| 1              | View a comprehensive list of albums | `GET` | `/albums` |
| 2              | Retrieve a list of all songs in a specified album | `GET` | `/albums/songs?album_name=<album_name>` |
| 3              | Find out the length of a specific song | `GET` | `/songs/length?song_name=<song_name>` |
| 4              | Access the full lyrics of a specific song | `GET` | `/songs/lyrics?song_name=<song_name>` |
| 5              | Discover which album a particular song belongs to | `GET` | `/songs/album?song_name=<song_name>` |
| 6              | Search for songs by name | `GET` | `/search/songs?name=<word>` |
| 7              | Search for songs by lyrics | `GET` | `/search/songs?lyrics=<word>` |
| 8              | Exit - the init JWT will be expired and a new one will be generated  | `POST` | `/exit` |

Schema from `Pink_Floyd_DB.txt`

```text
 # [Folow by the album name]::[Published year]

 *[Song name]::[singer]::[duration ]::[First line on the song]
 OR / AND
 *[Song name]::[singer]::[duration ]::instrumental
 ...
 [Last line on the song]
  *[Song name]::[singer]::[duration ]::[First line on the song]


  ....
 # Next Alboom ...
```


```bash
❯ ./test-endpoints.sh
+ BASE_URL=http://localhost:5000
+ test_endpoints
+ echo 'Testing endpoint for viewing a comprehensive list of albums'
Testing endpoint for viewing a comprehensive list of albums
+ curl http://localhost:5000/albums
[
  "the piper at the gates of dawn",
  "a saucerful of secrets",
  "more",
  "division bell",
  "the wall",
  "dark side of the moon",
  "wish you were here",
  "animals"
]
+ echo -e '\nTesting endpoint for retrieving a list of all songs in a specified album using query parameters'

Testing endpoint for retrieving a list of all songs in a specified album using query parameters
+ curl 'http://localhost:5000/albums/songs?album_name=The%20Wall'
[
  "in the flesh ?",
  "the thin ice",
  "another brick in the wall (part 1)",
  "the happiest days of our lives",
  "another brick in the wall (part 2)",
  "mother",
  "goodbye blue sky",
  "empty spaces",
  "young lust",
  "one of my turns",
  "don't leave me now",
  "another brick in the wall (part 3)",
  "goodbye cruel world",
  "hey you",
  "is there anybody out there ?",
  "nobody home",
  "vera",
  "bring the boys back home",
  "comfortably numb",
  "the show must go on",
  "in the flesh",
  "run like hell",
  "waiting for the worms",
  "stop",
  "the trial",
  "outside the wall"
]
+ echo -e '\nTesting endpoint for finding out the length of a specific song'

Testing endpoint for finding out the length of a specific song
+ curl 'http://localhost:5000/songs/length?song_name=Comfortably%20Numb'
{
  "length": "06:49",
  "song": "Comfortably Numb"
}
+ echo -e '\nTesting endpoint for accessing the full lyrics of a specific song'

Testing endpoint for accessing the full lyrics of a specific song
+ curl 'http://localhost:5000/songs/lyrics?song_name=Comfortably%20Numb'
{
  "lyrics": [
    "Hello,",
    "Is there anybody in there ?",
    "Just nod if you can hear me",
    "Is there anyone at home",
    "Come on now,",
    "I hear you're feeling down",
    "I can ease your pain",
    "And get you on your feet again",
    "Relax,",
    "I'll need some information first",
    "Just the basic facts",
    "Can you show me where it hurts ?",
    "There is no pain, you are receding",
    "A distant ship smoke on the horizon",
    "You are only coming through in waves",
    "Your lips move but I can't hear what you're saying",
    "When I was a child I had a fever",
    "My hands felt just like two balloons",
    "Now I've got that feeling once again",
    "I can't explain, you would not understand",
    "This is not how I am",
    "I have become comfortably numb",
    "O.K.,",
    "Just a little pin prick",
    "There'll be no more aaaaaaah !",
    "But you may feel a little sick",
    "Can you stand up ?",
    "I do, believe it's working, good",
    "That 'll keep you going through the show",
    "Come on, it's time to go.",
    "There is no pain, you are receding",
    "A distant ship smoke on the horizon",
    "You are only coming through in waves",
    "Your lips move but I can't hear what you're saying",
    "When I was a child",
    "I caught a fleeting glimpse",
    "Out of the corner of my eye",
    "I turned to look but it was gone",
    "I cannot put my finger on it now",
    "The child is grown",
    "The dream is gone",
    "I have become comfortably numb"
  ],
  "song": "Comfortably Numb"
}
+ echo -e '\nTesting endpoint for discovering which album a particular song belongs to'

Testing endpoint for discovering which album a particular song belongs to
+ curl 'http://localhost:5000/songs/album?song_name=Comfortably%20Numb'
{
  "album": "the wall",
  "song": "Comfortably Numb"
}
+ echo -e '\nTesting endpoint for searching for songs by name'

Testing endpoint for searching for songs by name
+ curl 'http://localhost:5000/search/songs?name=pig'
[
  "pigs on the wing (part one)",
  "pigs",
  "pigs on the wing (part two)"
]
+ echo -e '\nTesting endpoint for searching for songs by lyrics'

Testing endpoint for searching for songs by lyrics
+ curl 'http://localhost:5000/search/songs/lyrics?lyrics=brick%20in%20the%20wall'
[
  "another brick in the wall (part 1)",
  "another brick in the wall (part 2)"
]
+ echo -e '\nTesting endpoint shutdown server'

Testing endpoint shutdown server
+ curl -X POST http://localhost:5000/exit
{
  "message": "Shutting down server..."
}

home-assignment-magshimim/exercise-1 on  main [✘!?] took 5s
❯
```


Load into one data structure (dict) :
 

<br/>
<br/>

# Exercise - 2
Solution ar `exercise-2/solution.py`
![Alt text](images/exercise-2.png)
