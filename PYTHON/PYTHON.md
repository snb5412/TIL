## 환경 설치

1.  pip install bs4 ( Beautiful Soup )

2.  csv plugin install

****

## import os

1. os.**chdir('폴더 주소')** : 작업하고 있는 위치 변경

2. os.**listdir('폴더 주소')** : 폴더 내의 파일 리스트

3. os.**rename('현재 이름', '바꿀 이름')**

4. os.**path.splitext(filename)** : 파일명과 확장자명을 튜플로 return



<hr/>

## import csv

1. 쓰기

   1) csv.**writer(file)**

   2) csv.writer(file).**writerow(content)**

2. 읽기

   1) csv.**reader(file)**

   


<hr/>

## Scraping

1. req = requests.get(url, headers).text

   (headers = 개발자 도구 -> network -> 아무거나 클릭 -> User-Agent)

2. soup = BeautifulSoup(req, 'html.parser')

   -> BeautifulSoup : request 받은 html 문서를 선택자에 따라 parsing 해주는 라이브러리

3. 선택자 사용해서 select

<hr/>

