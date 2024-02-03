# დაწერეთ კალკულატორი, რომელიც შეგვეკითხება პირველ რიცხვს, შემდეგ მეორე რიცხვს, შემდეგ მათემატიკურ 
# ოპერატორს და შესაბამისი მათემატიკური ოპერატორის გამოყენებით დაგვიბეჭდავს შედეგს.

num1 = float(input("Please, input number 1: "))
num2 = float(input("Please, input number 2: "))
operator = input("Please, input math operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "//":
    print(num1 // num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Please, input correct math operator")