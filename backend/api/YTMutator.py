from urllib.parse import urlparse, parse_qs


class YouTubeMutator():
    def __init__(self, youtube_build):
        self.youtube_account = youtube_build
    
    def getAllUserPlaylists(self):
        part = 'id,snippet,status,contentDetails'
        playlists = self.youtube_account.playlists().list(part=part, mine=True).execute()['items']
        return playlists

    def getUserPlaylist(self, playlist_name):
        queried_playlists = self.youtube_account.playlists().list(
            part='id,snippet,status,contentDetails',
            mine=True
        ).execute()

        for playlist in queried_playlists['items']:
            if playlist['snippet']['title'] == playlist_name:
                return playlist
        return None

    def createUserPlaylist(self, playlist_name):
        '''
        Must insert a song to a playlist for it to display on the account from my testing.
        The playlist is created, it is just hidden in the "youtube.com/@USERNAME/playlists" page until it has at least 1 item in it.
        When adding to a playlist from a video page, then it will display all playlists even if they are empty.
        '''

        part = 'id,snippet,status,contentDetails'
        resource = {'kind': "youtube#playlist", "snippet": {'title': playlist_name, 'defaultLanguage': 'en'}}
        playlist_object = self.youtube_account.playlists().insert(part=part, body=resource).execute()
        return playlist_object

    def addSongToUserPlaylist(self, playlist_object, url):
        yt_song = self.getSongObject(url=url)
        part = 'id,snippet,status,contentDetails'
        insert_data = {
            'kind': 'youtube#playlistItem',
            'snippet': {
                'playlistId': playlist_object['id'],
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': yt_song['items'][0]['id']
                }
            }
        }
        self.youtube_account.playlistItems().insert(part=part, body=insert_data).execute()


    def getSongObject(self, url):
        '''
        Return a video object given a YouTube URL
        '''
        # Parse the video ID from the URL
        parsed_url = urlparse(url)
        video_id = parse_qs(parsed_url.query).get("v", [None])[0]

        if video_id:
            video_object = self.youtube_account.videos().list(
                part='id',
                id=video_id
            ).execute()
            return video_object
        else:
            print("ERROR - Invalid link")
            return None

    def updateUserPlaylistInfo(self, playlist_object: object):
        '''
        Make a playlist private and add a PlaylistExporter description to it
        '''
        part = 'id,snippet,status'
        update_data = {
            'id': playlist_object['id'],
            'snippet': {
                'title': playlist_object['snippet']['title'],
                'description': 'Created with PlaylistExporter',
            },
            'status': {
                'privacyStatus': 'public'
            }
        }
        self.youtube_account.playlists().update(part=part, body=update_data).execute()

    def deleteUserPlaylist(self, playlist_object):
        self.youtube_account.playlists().delete(id=playlist_object['id']).execute()