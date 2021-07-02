print("Hello Python")

# Separator 옵션 사용
print('t','e','s','t', sep='')

# End 옵션 사용 
print('Welcome to', end=' ')
print('black parade')

#format 사용 [], {}, ()
print('{} {}'.format('fuck', 'you'))
print('{0} {1} {0}'.format('fuck', 'you'))
print('{a} {b}'.format(a = 'fuck', b = 'you'))

#리스트
a = []
b = list()
c = [1,2,3,4]
d = [10,100,1000,1000000,1000000000000]
print(a,b,c,d)
print(d[0:1])
print(d[0:4])
print(d[0:65])

#튜플

a = ()
b = (1,)
c = (10,10,10)

# 딕셔너리 
# key : Value 

f = {'name' : 'kim', 'phone' : 'hello'}
print(f)
print(f.get('name'))
print(f.get('hi'))

#집합(set)
set1 = set() 
set2 = set([1,2,3,4,5,6])
set3 = set([1,3,4,5,6,7,8,8,8])
print(set1,set2,set3)