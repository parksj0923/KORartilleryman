'''1.1번, 2번, 3번 수포자의 정답지들을 리스트로 만들어야함
    1번의 경우 i번째를 5로 나눴을때 나머지 + 나머지가 0일때는 +1
    2번의 경우 홀수번째는 다 2, 짝수번째는 /2를 한 숫자를 4로 나눈 나머지를  [5,1,3,4] 여기서 뽑음
    3번의 경우 i//2로 몫을 구하고 %5번째의 index를 뽑아냄
    
2.반복문을 돌리면서 1,2,3의 정답 숫자를 센다
3.1,2,3의 정답 숫자를 비교후 return한다. 만약 숫자가 같은경우 오름차순으로 한다.'''


def mk1(i):
    if (i+1) % 5 == 0:
        return 5
    else:
        return (i+1)%5
    return 

def mk2(i):
    helper = [1,3,4,5]
    if i%2 == 0:
        return 2
    else:
        k = (i//2)%4
        return helper[k]
    return 


def mk3(i):
    helper = [3,1,2,4,5]
    k = (i//2)%5
    return helper[k]
    
def solution(answers):
    answer = []
    man1 =0
    man2 =0
    man3 =0
    
    for i in range(len(answers)):
        answer1 = mk1(i)
        answer2 = mk2(i)
        answer3 = mk3(i)
        if answer1 == answers[i]:
            man1 += 1
        if answer2 == answers[i]:
            man2 += 1
        if answer3 == answers[i]:
            man3 += 1
        #print(answer1,answer2,answer3)
    #print("answer",man1,man2,man3)
    temp = []
    temp.append(man1)
    temp.append(man2)
    temp.append(man3)
    temp.sort(reverse = True)
    #print(temp)
    if temp[0] == man1:
        answer.append(1)
    if temp[0] == man2:
        answer.append(2)
    if temp[0] == man3:
        answer.append(3)
    answer.sort()
        
            
    return answer
shit = [3,1,2,4,5,3,1,2,4,5,3,1,4,5,3,1,3,4,5,2,3,2,4,1,3,2,3,4,2,3,5,2,3,5,2,3,5,2,3,5,2,3,5,2,3,4,2,3,4,1,4,1]
print(solution(shit))
