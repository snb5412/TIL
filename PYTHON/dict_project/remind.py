# 1
# lunch = {
#     '중국집': '02'
# }

# 2
lunch = dict(중국집='02')

# 값 추가
lunch['분식집'] = '031'

idol = {
    'bts':{
        '지민':25,
        'RM':24
    }
}

# 랩 몬스터의 나이?
# print(idol['bts']['RM'])

# 딕셔너리 + 반복문
# 기본 활용

for key in lunch:
    print(key)
    print(lunch[key])

# .items()
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기
for value in lunch.values():
    print(value)

# key 만 가져오기
for key in lunch.keys():
    print(key)

