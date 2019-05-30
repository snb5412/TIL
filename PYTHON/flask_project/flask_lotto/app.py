import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    res = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = res.json()

    # 번호 6개 가져오기
    # winner = []
    # for i in range(1,7):
    #     winner.append(lotto[f'drwNo{i}'])

    # list comprehension
    winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]
    bonus = lotto['bnusNo']

    # 내 번호 리스트 만들기
    # my_number = random.sample(range(1,46), 6)
    my_number = [int(request.args.get(f'num{i}')) for i in range(1,7)]

    # 당첨번호와의 교집합
    correct = len(set(winner) & set(my_number))
    rank = '꽝'
    # 조건에 따라 1등부터 꽝까지 결과값을 lotto_result 로 보내준다.
    if correct == 3:
        rank = '5'
    elif correct == 4:
        rank = '4'
    elif correct == 5:
        if not bonus in my_number:
            rank = '3'
        else:
            rank = '2'
    elif correct == 6:
        rank = '1'

    return render_template('lotto_result.html', lotto_round=lotto_round, winner=f'{winner} + {bonus}', my_number=my_number, rank=rank)

if __name__=='__main__':
    app.run(debug=True)
