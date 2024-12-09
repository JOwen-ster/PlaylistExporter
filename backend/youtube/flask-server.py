import os
import flask
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from spotify import get_spotify_playlist_songs  # Import from your Spotify file
from youtube import youtube_search, create_youtube_playlist, add_to_youtube_playlist  # Import from your YouTube file

# Load environment variables from .env
load_dotenv()

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:5000/callback"

# YouTube credentials
CLIENT_SECRETS_FILE = "client_secrets_youtube_playlist_exporter.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Initialize Flask app
app = flask.Flask(__name__)
app.secret_key = os.urandom(12)

# Spotify login function
def spotify_login():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="user-library-read"
    ))
    return sp

@app.route('/')
def index():
    """Shows the main index page"""
    return flask.render_template('index.html')

@app.route('/authorize')
def authorize():
    """Initiates the Spotify OAuth2 authorization flow"""
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(
        access_type='offline', include_granted_scopes='true')
    flask.session['state'] = state
    return flask.redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    """Handles the OAuth2 callback and stores credentials"""
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    return flask.redirect('/PlaylistExporter')

@app.route('/PlaylistExporter')
def playlist_exporter():
    """Export a Spotify playlist to YouTube"""
    # Example playlist name
    spotify_playlist_name = "Your Spotify Playlist Name"
    youtube_playlist_name = "Your YouTube Playlist Name"
    
    # Get Spotify songs
    spotify_songs = get_spotify_playlist_songs(spotify_playlist_name)

    # Create YouTube playlist
    youtube_playlist_id = create_youtube_playlist(youtube_playlist_name)

    # Add each Spotify song to YouTube playlist
    for song in spotify_songs:
        query = f"{song.song_name} by {song.artist_name}"
        video_id = youtube_search(query)

        if video_id:
            add_to_youtube_playlist(youtube_playlist_id, video_id)
            print(f"Added {query} to YouTube playlist.")
        else:
            print(f"Could not find {query} on YouTube.")

    return flask.render_template('playlist_exported.html')

@app.route('/list_youtube_playlists')
def list_youtube_playlists():
    """List YouTube playlists"""
    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    request = youtube.playlists().list(
        part="snippet",
        mine=True
    )
    response = request.execute()
    playlists = response.get('items', [])
    return flask.jsonify(playlists)

if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPS verification
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run('localhost', 5000, debug=True)
