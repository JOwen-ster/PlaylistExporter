from pytube import YouTube
import requests
from requests import post
import base64
import json
from dotenv import load_dotenv
import os


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
clientID = os.getenv('clientID')
clientSecret = os.getenv('clientSecret')

# Youtube Data API 3 key AIzaSyB8vC1kJfXRW_5v0df9JBf4u9uuVwmwUOs
# Youtube Api being used to get video id from search
def getYT(search):
    global not_found
    api_url = 'https://www.googleapis.com/youtube/v3/search?key=YOUR_API_KEY&part=snippet&q={}r&type=video'
    api_url = api_url.format(search)
    try:
        data = requests.get(api_url)
        results = data.json()
        searchHits = results['pageInfo']['totalResults']
        if searchHits > 0:
            videoID = results['items'][0]['id']['videoId']
        else:
            not_found.append(search)
            return 'null'
        return videoID
    except Exception as e:
        print("An error occurred during YouTube search:", e)
        return 'null'


# pytube used to download video
# use return value of id from the getID function for the num parameter
def downloadVid(num):
    if num != 'null':
        url = "https://www.youtube.com/watch?v=" + num
        video = YouTube(url)
        video = video.streams.get_highest_resolution()
        video.download(output_path="/home/patrick/Documents/Downloaded_Songs")
    else:
        return

# changing file extensions from mp4 to mp3 
def filesToMp3():
    path = os.chdir("/home/patrick/Documents/Downloaded_Songs")
    for song in os.listdir(path):
        if (song[-3:]== "mp4"):
            old_name = song.removesuffix("mp4")
            new_name = old_name + "mp3"
            os.rename(song, new_name)
            print("Song", old_name, "has been converted to a mp3 file")

def getSpotifyToken():
    encoded = base64.b64encode((clientID + ":" + clientSecret).encode("ascii")).decode("ascii")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }
 
    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers, auth=(clientID, clientSecret))
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
        query_url + "?limit=50&offset={}"
        query_url.format(offset)
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
        videoidlist.append(videoID)
    print("These are all the songs from the Playlist")
    print(videoidlist)
    
    filesToMp3()
    print(track_id_list)
    print(videoidlist)
    print("These songs couldn't be downloaded")

    print(not_found)
    return 0

def spotifyOnly():
    link = input("Paste Spotify Link Here: ")
    token = getSpotifyToken()
    getTrackIDS(token, link)
    print(track_id_list)
    videoidlist = []
    for songID in track_id_list:
        search = trackSearch(songID)
        print(search)
        # videoID = getYT(search)
        # videoidlist.append(videoID)

spotifyOnly()

# main(playlist_link)
