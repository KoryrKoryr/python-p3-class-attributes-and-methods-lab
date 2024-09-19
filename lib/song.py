class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count
        self.add_song_to_count()
        
        # Add artist and genre
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        
        # Update artist and genre counts
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    # Class methods to retrieve data
    @classmethod
    def get_song_count(cls):
        return cls.count
    
    @classmethod
    def get_artists(cls):
        return cls.artists
    
    @classmethod
    def get_genres(cls):
        return cls.genres
    
    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
    
    @classmethod
    def get_genre_count(cls):
        return cls.genre_count
