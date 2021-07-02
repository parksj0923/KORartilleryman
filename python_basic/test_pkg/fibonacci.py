class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title
        
    def fib(n):
        a,b = 0,1
        while a <n:
            print(a, end =' ')
            a,b = b,a+b 
        print("")

        
    def fib2(n):
        result = []
        a,b = 0,1
        while a <n:
            result.append(a)
            a,b = b,a+b 
        return result
    
    
#단위 실행(독립적으로 파일을 실행)
#이 파일이 main일때만 실행함
#이 뜻은 다른 파일에서 이 파일을 실행할 경우 실행이 안됨
if __name__ == "__main__":
    Fibonacci.fib(10)
    print("Fibonacci:",Fibonacci.fib2(20))