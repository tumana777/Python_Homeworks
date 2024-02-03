# დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა


def main():
    string = input("Please, input string: ")
    symbol = input("Please, input symbol: ")
    
    print(symbol_counter(string, symbol))

def symbol_counter(str, sym):
    return str.count(sym)

main()