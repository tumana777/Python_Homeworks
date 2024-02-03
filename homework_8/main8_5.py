# დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს, ფუნქციაში 
# გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError). 
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი. 
# params:[1, 2, 3, 4, 5] 
# output: 120


from functools import reduce

lst = [1, 2, 3, 4, 5]

try:
    multi = reduce(lambda a, b: a * b, lst)
except TypeError:
    print("Something went wrong")
else:
    print(multi)