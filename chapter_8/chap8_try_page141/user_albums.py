""" Exercise 8-7 """

# Write a function called make_album()
def make_album(artist, album_title, number_of_songs_on_album=None):
    # Return a dictionary containing album information
    return {
        'artist': artist,
        'album_title': album_title,
        'Number of songs on an Album': number_of_songs_on_album
    }

"""
# Use the function to make three dictionaries representing different albums 
# & Print each return value to show that the dictionaries are storing the album information correctly.
print(make_album('artist1', 'album1'))
print(make_album('artist2', 'album2'))
print(make_album('artist3', 'album3'))
print(make_album('a', 'b', 10))
"""

# Write a while loop that allows users to enter an album’s artist and title.
running = True  # Control variable to keep the loop running

while running:
    # Prompt the user to enter the artist's name
    user_art = input('Enter artist name: ')
    
    # Prompt the user to enter the album's title
    user_album = input('Enter album title: ')
    
    # Call make_album() with the user’s input and print the created dictionary
    print(make_album(user_art, user_album))
    
    # Ask the user if they want to continue entering more albums
    # If the user enters anything other than 'yes', the loop will stop
    if input('Do you want to add another album? (yes/no): ').lower() != 'yes':
        running = False  # Stop the loop if the user inputs 'no'
