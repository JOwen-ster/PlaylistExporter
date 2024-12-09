import os
from googleapiclient.discovery import build
from spotify.spotify import SpotifySong, get_spotify_playlist_songs  # Import from the first file

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def youtube_search(video_query: str) -> str:
    """Searches YouTube for a video matching the query."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=video_query, part="snippet", maxResults=1, type="video"
    )
    response = request.execute()
    items = response.get("items", [])

    if not items:
        return None

    return items[0]["id"]["videoId"]


def create_youtube_playlist(title: str, description: str = "") -> str:
    """Creates a YouTube playlist."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {"title": title, "description": description},
            "status": {"privacyStatus": "private"},
        },
    )
    response = request.execute()
    return response["id"]


def add_to_youtube_playlist(playlist_id: str, video_id: str):
    """Adds a video to a YouTube playlist."""
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {"kind": "youtube#video", "videoId": video_id},
            }
        },
    ).execute()


def spotify_to_youtube(spotify_playlist_name: str, youtube_playlist_name: str):
    """Transfers songs from a Spotify playlist to a YouTube playlist."""
    spotify_songs = get_spotify_playlist_songs(spotify_playlist_name)
    youtube_playlist_id = create_youtube_playlist(youtube_playlist_name)

    for song in spotify_songs:
        query = f"{song.song_name} by {song.artist_name}"
        video_id = youtube_search(query)

        if video_id:
            add_to_youtube_playlist(youtube_playlist_id, video_id)
            print(f"Added {query} to YouTube playlist.")
        else:
            print(f"Could not find {query} on YouTube.")
