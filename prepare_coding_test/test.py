def solution(land):
    answer = land
    buf = []
    for i in range(1,len(land)):
        
        for j in range(4):
            
            for k in range(4):
                if j == k:
                    break
                else :
                    buf.append(land[i][j]+land[i-1][k])
                    print(j,k)
            print(buf)

            buf = []
    return max(answer[len(land)])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

solution(land)