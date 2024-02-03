# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი, 
# ააწყვეთ კალკულატორი, რომელიც გამოთვლის შესაბამის მოქმედებას, გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად 
# იქნება მათემატიკური ოპერატორები

def calculator(n1, n2, op):
    
    operators = {
        "+" : n1 + n2,
        "-" : n1 - n2,
        "*" : n1 * n2,
        "/" : n1 / n2,
        "**" : n1 ** n2,
        "//" : n1 // n2,
        "%" : n1 % n2
    }
    
    return f"{n1} {op} {n2} = {operators[op]}"

try:
    number1 = int(input("Please, input number 1: "))
    number2 = int(input("Please, input number 2: "))
    operator = input("Please, input operator: ")
    print(calculator(number1, number2, operator))
except ValueError:
    print("Please, input only integers!")
except KeyError:
    print("Please, input correct operator!")
except ZeroDivisionError:
    print("Cannot be divided by zero!")