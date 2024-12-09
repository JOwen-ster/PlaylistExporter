import requests
from requests import post
import base64
import json
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build



# IMPORTANT Global Variables 
# Working is Testing API Calls

# Test link to be used later
playlist_link = "https://open.spotify.com/playlist/2lBQEVNJIvSMT7q3T0GtZ8?si=ae4fa00666c04e70"
# Making variables to be global bc they are used in different functions
playlist_id = " "
token = " "
track_id_list = []
not_found = []
# clientID = os.getenv('clientID')
# clientSecret = os.getenv('clientSecret')
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
googleSecret = os.getenv('googleKey')


# Youtube Data API 3 key 
# Youtube Api being used to get video id from search
def getYT(search):
    global not_found
    api_url = F'https://www.googleapis.com/youtube/v3/search?key={googleSecret}&part=snippet&q={search}r&type=video&maxResults=1'
    youtube = build('youtube', 'v3', developerKey=googleSecret)
    try:
        # results = youtube.search().list(q='search', part='id,snippet', maxResults=1)
        # print(results)
        data = requests.get(api_url)
        results = data.json()
        # print(results)
        searchHits = results['pageInfo']['totalResults']
        if searchHits > 0:
            videoID = results['items'][0]['id']['videoId']
        else:
            not_found.append(search)
            return 'null'
        return videoID
    except Exception as e:
        print(results)
        print("An error occurred during YouTube search:", e)
        return 'null'

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