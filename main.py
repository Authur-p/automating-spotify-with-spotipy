import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from billboard_scrapping import *

# to authenticate a user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    cache_path='token.txt',
    scope='playlist-modify-private',
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_uri=os.environ.get('REDIRECT_URI'),
    show_dialog=True
))
user_id = sp.current_user()['id']
year = date_to_travel.split('-')[0]
song_uris = []

for song_name in top_songs:
    # generate tracks uri's'
    song_uri = sp.search(q=f"track:{song_name} year:{year}", type="track")
    # song_uri = sp.search(song_name,1,0,'track')
    try:
        # add those uri's' to a list
        song_uris.append(song_uri['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

# create playlist for the user
playlist = sp.user_playlist_create(user_id, f"{date_to_travel}Billboard 100",
                                   public=False, description=f"top 100 songs of the year {date_to_travel}")
# playlist id
playlist_id = playlist['id']

# adding songs to the playlist
add_track = sp.playlist_add_items(playlist_id, song_uris)
