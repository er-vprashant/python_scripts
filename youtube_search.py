#Author: Prashant 
#git: github.com/xprashantxx
#mail: xprashantxx@gmail.com
#Requirements: requests, BeautifulSoup

import os
import webbrowser
import requests
from bs4 import BeautifulSoup

songName = input("Enter the song : ")
songName = songName.replace(' ', '+')

# search for the best similar matching video
searchUrl='https://www.youtube.com/results?search_query='
url = searchUrl + songName
source_code = requests.get(url,timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the url of the video
songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]
link = song['href']
webbrowser.open('https://www.youtube.com' + link)
