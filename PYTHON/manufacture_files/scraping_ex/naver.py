import requests
from bs4 import BeautifulSoup


req = requests.get('https://www.naver.com/').text

soup = BeautifulSoup(req, 'html.parser')

tags = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

for tag in tags:
    print(tag.text)