# რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და
# დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს )


def sum_digits(number):
    
    num_to_str = str(number)
    
    if len(num_to_str) == 1:
        return(int(num_to_str))
    else:
        return int(num_to_str[0]) + sum_digits(int(num_to_str[1:]))

print(sum_digits(45689))

