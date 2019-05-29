import random
import requests
import json
from pprint import pprint

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()
# pprint(lottery)

winner = []

for i in range(1,7):
    winner.append(lottery[f'drwtNo{i}'])

bonus = lottery['bnusNo']

count = 1
# 내가 자동으로 산 복권 번호와 당첨번호(Winner) 교집합 개수 비교를 통해 등수 매기기
while True:

    my_number = random.sample(range(1,46), 6)

    winner_set = set(winner)
    my_number_set = set(my_number)

    correct_num = len(winner_set & my_number_set)

    if correct_num == 3:
        rank = 5

    elif correct_num == 4:
        rank = 4

    elif correct_num == 5:
        rank = 3

    elif correct_num == 6:
        if bonus in my_number:
            rank = 2
        else:
            rank = 1
            break

    count += 1

print(f'등수 : {rank} / 횟수 : {count} / 쓴 돈 : {count * 1000}')
