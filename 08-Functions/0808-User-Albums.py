def album(artist, title, songs_number=None):
    return f"{artist.title()} - {title.title()}, {songs_number} songs"


while True:
    print("\nPlease enter an artist name, a title and a number of songs(optional) successively:")
    print("(enter 'q' to quit)")

    artist_name = input("Artist name: ")
    if artist_name == "q":
        break

    title = input("Title: ")
    songs_number = input("Number of songs: ")
    if songs_number == "q":
        break

    print(album(artist_name, title, songs_number))
