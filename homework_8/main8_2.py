# დაწერეთ lambda ფუნქცია რომელიც იღებს სიას(list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

lst = [1, 2, 3, 4, 5, 6, 7]

odds = list(filter(lambda n: n % 2, lst))

print(odds) 

