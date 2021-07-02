#함수 정의 방법  
# def  함수명 (parameter)

#example
def hello(world):
    print("Hello",world)

hello("park")


#example2
#매개변수를 몇개 받을 지 모를때, 받는인자에따라서 함수변화가 필요할때
#*이 한개일 때는 튜플로 받음, *이 두개 일때는 딕셔너리로 받음-뒤에 예제
def args_func(*args):
    print(args)
    
args_func("kim")
args_func("kim","park")

#example3
#받은 인수를 튜플로 만들 때 인덱스 매기기 
def args_func2(*args):
    for i,v in enumerate(args):
        print(i,v)
        
args_func2("kim")
args_func2("kim","park")

#example4
def kwargs_func(**kwargs):
    print(kwargs)
    
kwargs_func(name1 = 'KIM')
kwargs_func(name1 = 'KIM', name2 = 'PARK')


#전체혼합
def example_mul(arg1,arg2, *args, **kwargs):
    print(arg1,arg2,args,kwargs)
example_mul(10,20)
example_mul(10,20,'kim','park',age1=25,age2=39)

#example6 
#매개변수들 설명
def func_mul3(x: int) -> list:
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1,y2,y3]
print(func_mul3(95))

#람다식 예제
#람다식 : 메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시 실행 (Heap 초기화) -> 메모리 초기화 

lambda_mul = lambda num : num * 10

print(lambda_mul())

