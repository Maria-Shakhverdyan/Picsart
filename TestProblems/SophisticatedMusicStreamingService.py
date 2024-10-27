from abc import ABC, abstractmethod
from typing import List

class Song:
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = length
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str): 
            raise TypeError("Title must be a string")
        if value == "":
            raise ValueError("Title cannot be empty")
        self.__title = value
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        if not isinstance(value, str): 
            raise TypeError("Artist must be a string")
        if value == "":
            raise ValueError("Artist cannot be empty")
        self.__artist = value
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, str): 
            raise TypeError("Length must be a string")
        if value == "": 
            raise ValueError("Empty length")
        self.__length = value
    
    def song_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Length: {self.length}"

class Album:
    def __init__(self, title, artist, release_date):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs: List[Song] = []
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str): 
            raise TypeError("Title must be a string")
        if value == "":
            raise ValueError("Title cannot be empty")
        self.__title = value
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        if not isinstance(value, str): 
            raise TypeError("Artist must be a string")
        if value == "":
            raise ValueError("Artist cannot be empty")
        self.__artist = value
    
    @property
    def release_date(self):
        return self.__release_date
    
    @release_date.setter
    def release_date(self, value):
        if not isinstance(value, str):
            raise TypeError("Release date must be a string")
        if value == "":
            raise ValueError("Release date cannot be empty")
        self.__release_date = value

    def add_song(self, song):
        self.songs.append(song)
    
    def album_info(self):
        song_titles = ", ".join(song.title for song in self.songs)
        return f"Album: {self.title}, Artist: {self.artist}, Release Date: {self.release_date}, Songs: {song_titles}"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs: List[Song] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str): 
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        self.songs.remove(song)
    
    def playlist_info(self):
        song_titles = ", ".join(song.title for song in self.songs)
        return f"Playlist: {self.name}, Songs: {song_titles}"

class Genre(ABC):
    @abstractmethod
    def genre_info(self):
        pass

class Rock(Genre):
    def genre_info(self):
        return "Genre: Rock"

class Pop(Genre):
    def genre_info(self):
        return "Genre: Pop"

class MusicOperation(ABC):
    @abstractmethod
    def play(self, song: Song):
        pass
    
    @abstractmethod
    def search(self, title: str):
        pass

class MusicPlayer(MusicOperation):
    def __init__(self, songs: List[Song]):
        self.songs = songs
    
    def play(self, song: Song):
        print(f"Playing {song.song_info()}")

    def search(self, title: str):
        for song in self.songs:
            if song.title == title:
                return f"Found: {song.song_info()}"
        return "Song not found."

if __name__ == "__main__":
    song1 = Song("Lonely Day", "SOAD", "3:05")

    album = Album("Greatest Hits", "Queen", "1981")
    album.add_song(song1)

    playlist = Playlist("My Favorites")
    playlist.add_song(song1)

    player = MusicPlayer([song1])

    player.play(song1)

    print(player.search("Bohemian Rhapsody"))
    
    print(playlist.playlist_info())
    print(album.album_info())
