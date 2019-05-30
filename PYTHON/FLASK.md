## Flask 설치

- pip install flask



## Flask Run

- 기본적으로 app.py 를 실행 시킴
  - 명령어 : flask run
- 만약 다른 이름일 경우 ( but, flask.py 는 안됌 )
  - 명령어 : FLASK_APP=**name**.py flask run
  - 또는 export FLASK_APP=hello.py 를 사용해서 한번만 입력하면 끝, 이후는 flask run 명령어로 실행



## Flask Import

- from flask import Flask 
- app = Flask(_ _ name _ _)



## Debug Mode

- 서버 재구동 없이 코드가 바뀌면 자동으로 서버에 적용 시켜줌

- if _ _ name _ _ == '_ _ main_ _':

  ​		app.run(debug=True)



## Rendering

- from flask import render_templete
- render_templete(넘겨줄 문서명, 변수)



## `__name__`

- 현재 스크립트 파일이 시작점인지 아니면 모듈인지 판단

- import 로 가져오면 이 값은 모듈의 이름이 됨 ( ex : app.py 라면 app )
- 직접 실행하면 이 값은 `__main__`이 됨



## GET & POST 방식

- get 의 경우 url 에 보내는 데이터 모두 노출

- post 의 경우 url 에 노출되지 않고 데이터 보냄

- get

  - request.args.get('name')

- post 

  - @app.route('', methods=['POST'])

  - request.form.get('name')

    