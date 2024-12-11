import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from dataclasses import dataclass
from typing import List


@dataclass
class SpotifySong:
    """Characteristics of a spotify object."""

    artist_name: str
    song_name: str


load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
scope = "user-library-read"
redirect_uri = "http://127.0.0.1:5000/"
user = "spotify"
user_playlists = {}
sp = None


def login_user() -> List[str]:
    """Logs in the user to Spotify and returns a list of playlist names."""
    global sp, user_playlists

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=redirect_uri,
            scope=scope,
        )
    )
    
    playlists = sp.current_user_playlists()["items"]
    
    # Populate the global dictionary with playlist names and URLs
    user_playlists = {playlist["name"]: playlist["href"] for playlist in playlists}
    
    # Return just the playlist names
    return list(user_playlists.keys())


    

def send_user_playlist(playlist_name: str) -> List[SpotifySong]:
    """Returns a list of SpotifySong objects containing song and artist names from the specified playlist."""
    global sp, user_playlists

    if not sp:
        raise ValueError("User is not logged in. Please log in first by calling login_user.")
    
    if playlist_name not in user_playlists:
        raise ValueError(f"Playlist '{playlist_name}' not found. Please fetch playlists again.")

    # Extract playlist URL and ID
    playlist_url = user_playlists[playlist_name]
    playlist_id = playlist_url.split("/")[-1]
    
    results = sp.playlist_tracks(playlist_id)
    all_user_songs = []
    
    for item in results.get("items", []):
        track = item["track"]
        artist_name = track["artists"][0]["name"]
        song_name = track["name"]
        all_user_songs.append(SpotifySong(artist_name=artist_name, song_name=song_name))
    
    return all_user_songs

