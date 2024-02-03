# დაწერეთ პითონის პროგრამა რომელიც ატრიბუტად მიიღებს ერთ რიცხვს და დაბეჭდავს 1-დან ამ რიცხვის ჩათვლით 
# მოქმედებებს: x**2, x**10, x**x შემდეგი სახით

def square(x):
    for num in range(1, x + 1):
        print(f"{num} * {num}".ljust(10), num ** 2)
        
        
def pow_10(x):
    for num in range(1, x + 1):
        print(f"{num} ^ 10".ljust(10), num ** 10)
    
def power(x):
    for num in range(1, x + 1):
        print(f"{num} ^ {num}".ljust(10), num ** num)
    
    
    
square(15)
print()
pow_10(15)
print()
power(15)