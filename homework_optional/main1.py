# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს შეაყვანინებს რიცხვს და დაგვიბეჭდავს ამ რიცხვის ყველაზე დიდ გამყოფს, 
# რომელიც თავად ამ რიცხვზე ნაკლებია.

num = int(input("Please, input number: "))

lst = []

def great_divider(number):
    for n in range(1, number):
        if number % n == 0:
            lst.append(n)
        
    return lst[-1]
print(great_divider(num))