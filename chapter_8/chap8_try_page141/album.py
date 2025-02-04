# Define a function called make_album that creates a dictionary with album information
def make_album(artist, album_title, number_of_songs_on_album=None):
    # Return a dictionary with artist, album title, and optionally, the number of songs
    return {
        'artist': artist,
        'album_title': album_title,
        'Number of songs on an Album': number_of_songs_on_album
    }

# Use the function to create and print three album dictionaries without specifying the number of songs
print(make_album('artist1', 'album1'))  # Prints: {'artist': 'artist1', 'album_title': 'album1', 'Number of songs on an Album': None}
print(make_album('artist2', 'album2'))  # Prints: {'artist': 'artist2', 'album_title': 'album2', 'Number of songs on an Album': None}
print(make_album('artist3', 'album3'))  # Prints: {'artist': 'artist3', 'album_title': 'album3', 'Number of songs on an Album': None}

# Create and print an album dictionary with the number of songs specified
print(make_album('a', 'b', 10))  # Prints: {'artist': 'a', 'album_title': 'b', 'Number of songs on an Album': 10}
