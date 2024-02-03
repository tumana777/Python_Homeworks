# დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს ტექსტის შეყვანას და თუ შეყვანილი ტექსტი არის პალინდრომი დაბეჭდეთ 
# “შეყვანილი ტექსტი არის პალინდრომი” თუ არა, მაშინ დაბეჭდეთ “შეყვანილი ტექსტი არ არის პალინდრომი”

text = input("Please, input text: ")

middle = int(len(text)/2)

part1 = text[:middle]

if len(text) % 2 == 0:
    part2 = text[middle:]
else:
    part2 = text[middle + 1:]

part2_reversed = part2[::-1]

if part1 == part2_reversed:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")