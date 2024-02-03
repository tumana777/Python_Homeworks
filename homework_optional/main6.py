# დაწერეთ პითონის ფუნქცია რომელიც ატრიბუტად მიიღებს ინტეჯერებისგან შემდგარ ლისტს, 
# ლისტში შესაძლოა იყოს დუბლიკატები, ფუნქციამ უნდა დააბრუნოს ლისტი დუბლიკატების გარეშე


lst = [8, 9, 2, 4, 2, 25, 10, 2, 20, 25, 100, 9, 25, 50, 100]

def rm_dubl(arr):
    unique = []
    for elem in arr:
        if elem not in unique:
            unique.append(elem)
    return unique

print(rm_dubl(lst))
