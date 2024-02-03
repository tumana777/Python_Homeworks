# დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს(ending). 
# დააბრუნეთ მხოლოდ ის სიის ელემენტები, რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError)
# params: ['hello', 'world', 'coding', 'nod'], 'ing' 
# outputs: ['coding']

lst = ['hello', 'world','coding', 'nod']
ending = "ing"

try:
    findEnding = list(filter(lambda n: n.endswith(ending), lst))
except TypeError:
    print("Something went wrong")
else:
    print(findEnding)