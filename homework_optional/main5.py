# დაწერეთ პროგრამა რომელიც მომხმარებელს შეაყვანინებს რიცხვს და დაგვიბეჭდავს ეს რიცხვი არის თუ არა მარტივი, 
# თუ არ არის დაგვიბეჭდავს ეს არის რთული რიცხვი და დაბეჭდავს ასევე მის გამყოფებს

number = int(input("Please, input number: "))

lst = []

def simp_or_comp(num):
    for n in range(1, num + 1):
        if num % n == 0:
            lst.append(n)
            
    if len(lst) == 2 or num == 1:
        return f"{num} is simple number"
    elif len(lst) > 2:
        return f"{num} is complex number and its deviders are {tuple(lst)}"
    else:
        return "Please, input a natural number"

print(simp_or_comp(number))