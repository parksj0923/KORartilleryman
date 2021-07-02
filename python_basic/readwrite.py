#파일 읽기, 쓰기
#읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
#.. : 상대경로, . : 절대 경로 
#./resource이렇게 하면 지금 내 디렉토리가 기준으로 /resource를 들어가는거임
#기타 : https://docs.python.org/3.7/library/functions.html#open 


#파일 읽기

#예시1 
f = open('./resource/review.txt','r')
content = f.read()

print(content)

#반드시 close리소스 반환
f.close()


print("-----------------------------------------------------------------------------------")
#예시2
#close 안해도 알아서 with문 안에서 해결해줌
with open('./resource/review.txt','r') as f:
    c = f.read()
    print(c)

    
print("-----------------------------------------------------------------------------------")
#예시3
with open('./resource/review.txt','r') as f:
    print(iter(f))
    score = []
    for line in f:
        score.append(int(line))
    print(score)