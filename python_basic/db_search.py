# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('./resource/database.db') #본인 db경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n',c.fetchone())
# print('One -> \n',c.fetchone())

#지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

#전체 로우 선택
# print('All -> \n', c.fetchall())



#순회1
'''ch = 1
for row in c.fetchall():
    print('retreieve > ', ch, row)
    ch +=1 '''

#순회2
for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print(row)




print()


# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?',param1)
print('param1',c.fetchone())

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' %param2)
print('param1',c.fetchone())

# WHERE Retrieve3--딕셔너리이용
c.execute('SELECT * FROM users WHERE id=:Id',{"Id": 5})
print('param1',c.fetchone())

# WHERE Retrieve4
param4 = (3,5)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4',c.fetchall())


#Dump 출력- 데이터베이스 백업
with conn:
    with open('./resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print('Dump Print Complete')


#with에서 conn close까지 호출되어서 따로 conn.close안해도됨


