from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

rawdata = conn.read()
page_content = rawdata.decode()
soup = BeautifulSoup(page_content, "html.parser")

sec = soup.find("section", "section chart-grid")
li_list = sec.find_all("li")  
top_list =[]
for li in li_list:
    song_name = li.h3.a.string
    artist_name = li.h4.a.string
    top = {
        "A. Song": song_name,
        "B. Artist": artist_name    
    }
    top_list.append(top)

    x = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    }
    dl = YoutubeDL(x)
    dl.download([song_name + " - " + artist_name])

pyexcel.save_as(records = top_list, dest_file_name = "top_itune_songs.xlsx")

