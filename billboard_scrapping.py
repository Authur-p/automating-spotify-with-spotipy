from bs4 import BeautifulSoup
import requests

date_to_travel = input('what day are you looking for. use format YYYY-MM-DD: ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date_to_travel}/')

top_songs = []
soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select('li #title-of-a-story')
for song in songs:
    top_song = song.getText().replace('\n', '').replace('\t', '')
    top_songs.append(top_song)
