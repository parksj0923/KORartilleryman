# 파이썬 데이터 베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# sqlite3-버전확인
# print('sqlite3.version : ',sqlite3.version)
# print('sqlite3.sqlite_version :', sqlite3.sqlite_version)

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# DB 생성 & Auto Commit(데이터의 삽입 변경등을 메모리에 저장하고 있다가 영구반영을 할려면 commit을 해야한다)
# Rollback은 되돌리는것
# isolation_level=None을 하면 auto commit활성화
conn = sqlite3.connect('./resource/database.db', isolation_level=None)

# Cursor, 말그대로 커서, 읽는 부분을 나타냄
c = conn.cursor()
# print('Cursor Type :', type(c))


# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com','010-0000-0000','Kim.com',?)",(nowDatetime,))
# nowdatetime과 ?를 튜플로 매칭시켜서 삽임
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2,'Park', 'Park@daum.net', '010-9889-8331','Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-9838-3333', 'Lee.com', nowDatetime),
    (4, 'cHO', 'Cho@naver.com', '010-3333-2222', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-2222-3333', 'Yoo.com', nowDatetime)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
#c.execute("DELETE FROM users")
print("users db deleted :", c.execute("DELETE FROM users").rowcount)

# commit :  isolation_level = None일 경우 자동 반영(오토커밋)

#만약 안넣었다면 
#conn.commit

#접속해제
c.close()

