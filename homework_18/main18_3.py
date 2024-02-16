'''
დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი, 
რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი
'''
def commision(func):
    def wrapper(*args, **kwargs):
        bal = args[0]
        am = args[1]
        if am + 1 <= bal:
            return func(bal-1, am)
        else:
            return 'Insufficient balance'
    return wrapper

@commision
def transaction(balance, amount):
    return f'Your balance was ${balance + 1}, transaction is ${amount}, commision is ${1},so balance remaining ${balance - amount}.'

print(transaction(21, 10)) 