# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და
# დააბრუნებს მის შებრუნებულ (revers) სტრიქონს ( მაგალითად input:Hello Output: olleH)

def reverse(string):
    
    if len(string) == 0:
        return string
    else:
        return string[-1] + reverse(string[:-1])


print(reverse("Hello, world"))

