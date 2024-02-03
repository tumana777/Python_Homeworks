# დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. 
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even’ თუ კენტია ‘odd’

num = int(input("Please, input number: "))

if num % 2 == 0:
    print("Entered number is even")
else:
    print("Entered number is odd")