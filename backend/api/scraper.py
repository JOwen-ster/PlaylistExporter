import requests
from dotenv import load_dotenv
import os
import spotify

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_yt_links(search_object, google_api_key):
    youtube_links = []
    not_found = []

    base_url = "https://www.googleapis.com/youtube/v3/search"
    
    for song in search_object:
        artist = song.artist_name
        song_name = song.song_name
        search_query = f"{song_name} by {artist}"
        
        params = {
            "key": google_api_key,
            "part": "snippet",
            "q": search_query,
            "type": "video",
            "maxResults": 1
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            results = response.json()
            
            # Validate response structure
            if results.get("pageInfo", {}).get("totalResults", 0) > 0:
                video_id = results["items"][0]["id"]["videoId"]
                youtube_links.append(video_id)
            else:
                not_found.append(search_query)
        except requests.exceptions.RequestException as e:
            print(f"Error during YouTube search for '{search_query}': {e}")
            not_found.append(search_query)
    
    return youtube_links


#spotifySongs = spotify.send_user_playlist("test")

#youtubeLinks = get_yt_links(spotifySongs, GOOGLE_API_KEY)

#print(youtubeLinks)