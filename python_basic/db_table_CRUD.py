# 파이썬 데이터베이스 연동
# 테이블 데이터 수정 및 삭제

import sqlite3
#DB생성 (파일)
conn = sqlite3.connect('./resource/database.db')

#Cursor 연결
c = conn.cursor()

#데이터 수정1
#c.execute("UPDATE users SET username = ?  WHERE id =?",('niceman',2))

#데이터 수정1
#c.execute("UPDATE users SET username = :name  WHERE id =:id",{"name" : 'goodman',"id":5})

#중간데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)


#테이블 전체 데이터 삭제
print("users db deleted:", conn.execute("DELETE FROM users").rowcount,"rows")





conn.commit()

c.close()