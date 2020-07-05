# Simple rest server
네이버 검색 API를 실습하기 위한 간단한 REST SERVER 입니다.

## 레포지토리 클론
```shell
git clone https://github.com/Aqudi/Simple-rest-server.git
cd Simple-rest-server
```

## 네이버 검색 API 키 입력
constants.py 파일을 열고 발급받은 CLIENT_ID와 CLIENT_SECRET 을 적어줍니다.

## 패키지 설치
```shell
# 윈도우
pip install -r requirements.txt

# 우분투, Mac
pip3 install -r requirements.txt
```

## 서버 실행
``` shell
uvicorn main:app --reload  
```

## 테스트
아래 페이지에 들어가서 Swagger UI로 API를 테스트해볼 수 있다.


http://127.0.0.1:8000/docs
