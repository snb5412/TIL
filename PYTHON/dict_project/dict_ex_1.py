'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
sum = 0
for value in score.values():
    sum = sum + value

avg = sum / len(score)
print(avg)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sum = 0
cnt = 0
for key, value in scores.items():
    for value2 in value.values():
        sum = sum + value2
        cnt += 1

print(sum / cnt)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
'''
for key, value in city.items():
    temperature = 0
    for temp in value:
        temperature = temperature + temp

    # print(key, ' : ', temperature / len(value))
    print(f'{key} : {temperature/len(value)}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
cnt = 0
hot = 0
cold = 0
hot_city = ''
cold_city = ''
for key, value in city.items():
    if cnt == 0:
        hot = max(value)
        cold = min(value)
        hot_city = key
        cold_city = key
        cnt += 1
    else:
        if min(value) < cold:
            cold = min(value)
            cold_city = key

        if max(value) > hot:
            hot = max(value)
            hot_city = key

print(f'가장 추운 도시 : {cold_city}\n가장 더운 도시 : {hot_city}')
# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
check = 0
for temp in city['서울']:
    if temp == 2:
        check = 1
        break

if check == 1:
    print('Yes')
else:
    print('No')

print(5 in city['서울'])