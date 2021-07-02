#1 아래 문자열의 길이를 구해보세요
q1 = "asldkfja;sdlkfja;dfklajdf;lkajd;flkajsd"

print(len(q1))

#2 print 함수를 사용해서 아래와 같이 출력해보세요
# apple;orange;banana;lemon  

print("apple;orange;banana;lemon")

#3 화면에 *기호 100개를 표시하세요  
print('*'*100)

#4 문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요
print(int(30))
print(float(30))
print(complex(30))
print(str(30))

#5 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요  
a = "Niceman"
print(a[-3:])

#1.아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.a  
q1 = {"봄":"딸기", "여름":"토마토", "가을":"사과"}

for i in q1.keys():
    if i == "가을":
        print(q1[i])

#2. 아래 딕셔너리에서 '사과'가 포함되어있는지를 확인하세요
q2 = {"봄":"딸기", "여름":"토마토", "가을":"사과"}

for j in q2.keys():
    if q2[j]=="사과":
        print("include")
