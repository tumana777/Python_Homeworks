# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს და 
# დაგვიბრუნებს ფაქტორიალს ამ რიცხვის ჩათვლით.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))