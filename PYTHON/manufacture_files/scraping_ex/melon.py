import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

req = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = BeautifulSoup(req, 'html.parser')

songs = soup.select('#lst50')

with open('melonchart.txt', 'w', encoding='utf-8') as f:
    for song in songs:
        rank = song.select_one('.rank').text.zfill(2)
        name = song.select_one('.ellipsis.rank01 > span > a').text
        singer = song.select_one('.ellipsis.rank02 > a').text

        f.write(f'{rank} / {name} / {singer}\n')