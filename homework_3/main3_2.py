# დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum =0,
# შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე
# სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს , რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

total_sum = 0

while True:
    userInput = input("Please, input positive number: ")
    
    if userInput != "sum":
        num = float(userInput)
        if num >= 0:
            total_sum += num
        else:
            print("Input number is negative!")
            continue
    else:
        print(f"Total sum is: {total_sum}")
        break
