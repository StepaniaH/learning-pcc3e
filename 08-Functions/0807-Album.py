def album(artist, title, songs_number=None):
    return f"{artist} - {title}, {songs_number} songs"


print(album("The Beatles", "Abbey Road"))
print(album("The Beatles", "Abbey Road", 1))
print(album("The Beatles", "Abbey Road", songs_number=2))
