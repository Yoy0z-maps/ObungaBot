# 동기화

맥미니, 맥북 json, key.py 공유해야함

# ISSUE

1. Error 1
   인수를 user: discord.User로 받으면(디스코드에서는 @닉네임 형식) user.name이 닉네임이 아니라 닉네임 밑 아이디를 말하는 것이 됨
   회원 가입을 할 때 author.name은 서버 이름임
   회원 가입 구조를 먼저 바꿔야함
   문서 이름을 int형식 Discord고유 아이디로
   그 다음 유저의 닉네임을 필드에 추가 하는 방식으로 바꿔야함
2. Error 2
   만료된 API_KEY 갱신하기
3. Error 3
   웹 크롤링 하는 거 url이나 html요소 바뀐 것들 업데이트

# 개선

1. 사진 기존에 imgul을 통한 url 방식보다 firestorage사용하기
2. 도박 시스템에 버튼 UI 추가하기
