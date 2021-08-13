def move(n,start,end):
    print('{}번원반을 {}에서 {}로 옮기세요'.format(n,start,end))

def hanoi(n,start,end,middle):
    if n == 1:
        move(1,start,end)
    else:
        hanoi(n-1,start,middle,end)
        move(n,start,end)
        hanoi(n-1,middle,end,start)
    
hanoi(6,'A','C','B')