# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს სტრინგებისგან შემდგარ ლისტს, 
# ფუნქციამ უნდა შეაბრუნოს სტრინგის რეგისტრები და დააბრუნოს შებრუნებული რეგისტრებით შემდგარი ლისტი

def changeCase(lst):
    lst1 = [elem.swapcase() for elem in lst]
        
    return lst1

list1 = ["Green", "Blue", "rED"]

print(changeCase(list1))