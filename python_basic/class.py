#클래스는 속성과 메소드로 구성되어 있음
#속성은 클래스 안의 단순 변수
#메소드는 클래스안의 함수

#메소든 클래스안에 들어있는 함수
#인스턴스는 실체, 클래스는 부류
#스케이트 타는 사람=클래스, 김연아 = 인스턴스
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
#인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 사용 

#클래스 선언 
#clas 클래스명: 
#    함수
#    함수
#    함수

#ex1
#아무것도 안 넣고 class 선언할 때 pass넣으면 에러 안뜸
class Test:
    pass

class UserInfo:
    #속성, 메소드
    def __init__(self):
        print("초기화")

user1 = UserInfo()

class UserInfo2:
    #속성, 메소드
    def __init__(self, name):
        print("초기화2")
        self.name = name
    def user_info_p(self):
        print("name :",self.name )
        
user2 = UserInfo2("PARK")
user2.user_info_p()

#self의 의미
#self는 인스턴스를 가르킬때 사용된다.
#self를 사용안하면 메소드가 클래스 자체의 메소드가 되어버린다.
#즉 self를 쓰면 네임스페이스가 생긴다.

class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 called!')
        
self_test = SelfTest()
#self_test.function1() --에러발생, function1은 인스턴스의 함수가 아닌 클래스의 함수가 되어버림
SelfTest.function1()
self_test2 = SelfTest()
self_test2.function2()




