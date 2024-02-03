# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def main():
    fib_num = int(input("Please, input number of Fibonacci sequence: "))
    
    print(fibonacci(fib_num))

def fibonacci(n):
    begin = 0
    next = 1
    fib = 0
    list1 = []

    for i in range(n):
        list1.append(fib)
        fib = begin + next
        next = begin
        begin = fib
        
    return list1

main()