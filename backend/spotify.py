from dataclasses import dataclass
from typing import List


@dataclass
class SpotifySong:
    """Characteristics of a spotify object."""

    artist_name: str
    song_name: str


@dataclass
class SpotifyUtilizer:
    """Holds a list of SpotifySong objects."""

    list_of_songs: List[SpotifySong]


"""
TODO:
def login_user()
def return_all_playlists()
def send_user_playlist()
"""
