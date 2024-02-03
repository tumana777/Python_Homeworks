# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს სამის ჯერად რიცხვებს, ამის შემდეგ დაწერეთ ფუნქცია, რომელსაც 
# ატრიბუტებად გადაეწოდება ლისტი და ლამბდა ფუნქცია, ხაზობრივი ძიების და ლამბდა ფუნქციის დახმარებით შეავსეთ 
# ახალი ლისტი(ინდექსებით) და დააბრუნეთ მოცემული ლისტი.
# (ფუნქციამ უნდა დააბრუნოს ლისტი, რომელშიც შენახული იქნება სამის ჯერადი რიცხვების ინდექსები)

from random import randint

def randNums(from_, to, qty=100):
    
    return [randint(from_, to) for _ in range(qty)]

lst = randNums(0, 200)

print(f"Original list:\n {lst}")

x = lambda n: n % 3 == 0

lst1 = []

def indexes(arr, func):
    
    for i, e in enumerate(arr):
        if func(e):
            lst1.append(i)
            
    return lst1
    
print(f"\nIndexes of numbers devided by 3 without remainder are:\n{indexes(lst, x)}")