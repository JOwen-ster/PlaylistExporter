import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from dataclasses import dataclass
from typing import List

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:5000/"
SPOTIFY_SCOPE = "user-library-read"


@dataclass
class SpotifySong:
    """Represents a Spotify song."""
    artist_name: str
    song_name: str


def spotify_login():
    """Logs the user into Spotify."""
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope=SPOTIFY_SCOPE,
        )
    )


def get_spotify_playlist_songs(playlist_name: str) -> List[SpotifySong]:
    """Fetches songs from a Spotify playlist."""
    sp = spotify_login()
    playlists = sp.current_user_playlists()
    playlist_url = None

    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            playlist_url = playlist["href"]
            break

    if not playlist_url:
        raise ValueError(f"Playlist {playlist_name} not found.")

    playlist_id = playlist_url.split("/")[-1]
    results = sp.playlist_tracks(playlist_id)
    songs = []

    for item in results.get("items"):
        track = item["track"]
        artist_name = track["artists"][0]["name"]
        song_name = track["name"]
        songs.append(SpotifySong(artist_name=artist_name, song_name=song_name))

    return songs


print(get_spotify_playlist_songs("random"))  # Example usage