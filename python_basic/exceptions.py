#파이썬 예외처리 이해

#예외종류
#문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요

#1.SyntaxError : 잘못된 문법   
#    print('Test)
#    if True
#         pass
#    x=>y 

#2.NameError : 참조변수 없을 때
#a=5, b=10
#print(c)


#3.ZeroDivisionError : 0 나누기 에러 

#4.IndexError : 인덱스 범위 오버 


#5.KeyError : 없는키를 부를때
#그냥 dic['key'] 하지말고 dic.get('key')습관을 들여 에러를 없애자

#6.AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외 

#7.ValueError: 참조값이 없을 때 발생 

#8.FileNotFoundError : 파일이 없을때 나는 에러

#9.TypeError : 타입이 안맞을때 나는 에러      

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩 
#그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)


#예외 처리 기본
#try: 에러가 발생할 가능성이 있는 코드 실행
#except : 에러명1
#except : 에러명2 
#else : 에러가 발생하지 않았을 경우 실행
#finally : 항상 실행
#except Exception: 도 그냥 except:과 같은 의미임-마지막에 어떤에러가 뜰지 모를때 넣어주면 에러발생기 다 잡힘
#except as l: 이렇게 alias를 넣어주면 print(l)을 통해서 에러 이름을 알아서 넣어줌

#예제 1

name = ['Kim','Lee','Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it in name'.format(z,x+1))

except ValueError: #어떤에러가 발생할지 모르는 경우에는 굳이 except뒤에 붙일 필요 없음
    print('Not found it! - Occurred ValueError!')

else:
    print('there are no errors')
finally:
    print('finally')
    

#예외 발생 : raise
#raise 키워드로 예외 직접 발생
#원하는 에러를 발생시킬 수 있음  
try:
    a = 'cho'
    if a=='Kim':
        print("ok 허가")
    else:
        raise ValueError
except ValueError:
    print( 'there is a problem')
except Exception as l:
    print(l)
else:
    print( 'end')
    

