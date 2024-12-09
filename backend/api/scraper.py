import requests
from dotenv import load_dotenv
import sys
import os
import spotify


# Test link to be used later
playlist_link = "https://open.spotify.com/playlist/2lBQEVNJIvSMT7q3T0GtZ8?si=ae4fa00666c04e70"
playlist_id = " "
token = " "
track_id_list = []
not_found = []
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
googleSecret = os.getenv('googleKey')


# Youtube Data API 3 key 
# Youtube Api being used to get video id from search

import requests

def get_yt_links(search_object, google_api_key):
    """
    Searches for YouTube video links based on a list of Spotify songs.
    
    Args:
        search_object (list[SpotifySong]): A list of SpotifySong objects with artist and song_name attributes.
        google_api_key (str): Your YouTube Data API key.
    
    Returns:
        dict: A dictionary containing 'youtube_links' (list of links) and 'not_found' (list of failed searches).
    """
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
                youtube_links.append(f"https://www.youtube.com/watch?v={video_id}")
            else:
                not_found.append(search_query)
        except requests.exceptions.RequestException as e:
            print(f"Error during YouTube search for '{search_query}': {e}")
            not_found.append(search_query)
    
    return {
        "youtube_links": youtube_links,
        "not_found": not_found
    }


spotifySongs = spotify.send_user_playlist("si playlist")

youtubeLinks = get_yt_links(spotifySongs, googleSecret)

print(youtubeLinks)

'''
def getSpotifyToken():
    encoded = base64.b64encode((SPOTIFY_CLIENT_ID + ":" + SPOTIFY_CLIENT_SECRET).encode("ascii")).decode("ascii")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }

    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
    json_response = json.loads(response.content)
    global token 
    token = json_response["access_token"]
    return token
    

def getAuthHeader(token):
    return {"Authorization": "Bearer " + token}

def getTrackIDS(token, link): 
    global track_id_list
    # Spotify api setup and authentication
    playlist_url = "https://api.spotify.com/v1/playlists/"
    headers = getAuthHeader(token)
    
    playlist_id = link.split("playlist/")[1]
    head, sep, tail = playlist_id.partition("?")
    playlist_id = head
    query_url = playlist_url + playlist_id + "/tracks"
    offset = 0
    total = 0
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)
    total_songs = 0
    num_tracks = json_result['total']
    loop = int(num_tracks / 50)
    if num_tracks % 50 > 1:
        loop += 1
    for i in range(loop): # loop through requests 50 at a time while adding to offset
        query_url = query_url + "?limit=50&offset={}".format(offset)
        
        result = requests.get(query_url, headers=headers)
        json_result = json.loads(result.content)
        for j in range(50):
            if num_tracks > 0:
                track_id_list.append(json_result['items'][j]['track']['id'])
                num_tracks -= 1
                total_songs += 1
        head, sep, tail = query_url.partition("?")
        query_url = head
        offset += 50

def trackSearch(id):
    url = "https://api.spotify.com/v1/tracks/"
    query_url = url + id
    # print(query_url)
    header = getAuthHeader(token)
    result = requests.get(query_url, headers=header)
    json_result = json.loads(result.content)
    name = json_result['name']
    artist = json_result['artists'][0]['name']
    search = name + " by " + artist
    return search

def main(link):
    token = getSpotifyToken()
    playlist_link = link
    getTrackIDS(token, playlist_link)
    print(track_id_list)
    videoidlist = []
    for songID in track_id_list:
        search = trackSearch(songID)
        videoID = getYT(search)
        if videoID != "null":
            videoidlist.append(videoID)
            print("https://www.youtube.com/watch?v="+ videoID)
        # downloadVid(videoID)
    print("These are all the songs from the Playlist")
    print(videoidlist)
    
    
    # filesToMp3()
    # print(track_id_list)
    # print(videoidlist)
    # print("These songs couldn't be downloaded")

    print(not_found)
    return 0

def spotifyOnly():
    link = playlist_link
    token = getSpotifyToken()
    getTrackIDS(token, link)

    videoidlist = [trackSearch(song_id) for song_id in track_id_list]
    print(videoidlist)
    print(videoidlist)
    return videoidlist

# spotifyOnly()

main(playlist_link)

'''