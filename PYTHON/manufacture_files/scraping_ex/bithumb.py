import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bithumb.com/').text

soup = BeautifulSoup(req, 'html.parser')

# namelists = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
# pricelists = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')
# with open('coin.txt', 'w', encoding='utf-8') as f:
#     for i in range(len(namelists)):
#         f.write(f'{namelists[i].text} / {pricelists[i].text}\n')


lists = soup.select('.coin_list tr')


with open('coin.txt', 'w', encoding='utf-8') as f:
    for list in lists:
        name = list.select_one('td:nth-of-type(1) a strong').text.replace(' NEW', '').strip()
        price = list.select_one('td:nth-of-type(2) strong').text.strip()
        f.write(f'{name} / {price}\n')