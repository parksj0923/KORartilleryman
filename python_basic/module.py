#module과 package
#module은 필요한것들을 만들어 놓은 함수들의 모임
#package는 abs()의 모음


#test_pkg폴더안에 fibonacci파일에서 Fibonacci 클래서 참조
from test_pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))

#문제는 Fibonacci이름을 출력할때 Fibonacci.title하면 에러
#그 이유는 title속성은 def __init__안에 들어 있기 때문에 클래스를 생성해줘야함
print("ex3 : ", Fibonacci().title)

#만든 파일에서 독립적으로 파일을 실행해봐야 할 때가 있음
#단위 실행(독립적으로 파일을 실행)
#fibonacci 파일을 참고