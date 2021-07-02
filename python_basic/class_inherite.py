#클래스 상속 

#슈퍼클래스(부모) 및 서브클래스(자식) -> 자식 클래서는 부모클래서의 모든 속성, 메소드 사용 가능

#상속 방법은 자식 클래스를 만들때 매개변수에 부모클래스를 넣으면 됨

#슈퍼클래스
class Car:
    """parent Class"""
    def __init__(self,tp,color):
        self.type = tp
        self.color = color
        
    def show(self):
        return 'Car Class "show Method"'

#서브클래스
class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" %self.car_name
    
#서브클래스
class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" %self.car_name
    
#일반사용 
model1 = BmwCar('520d', 'sedan', 'red') 

print(model1.color) #super class에서 가져옴
print(model1.type)  #super class에서 가져옴
print(model1.car_name)  #sub class에서 가져옴
print(model1.show())  #super class
print(model1.show_model())


#Method Overriding(오버라이딩)
#부모클래스에 있는 메소드를 자식클래스에 이름을 똑같이해서 메소드를 만든다면 
#인스턴스에서 메소드를 호출하면 부모클래스의 메소드가 아닌 자식클래스에 새롭게 정의된 메소드를 호출한다.
#부모 메소드를 다시호출하고 싶으면 super.메소드 이렇게 다시 만들면됨



#상속 정보를 보고 싶을때
#class.mro()사용
#왼쪽에서 오른쪽으로 상속된다고 생각하면됨

print(BmwCar.mro())







