# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს შეაყვანინებს ერთ სტრინგს და ერთ რიცხვს, 
# გამოიყენეთ ცეზარის შიფრი და დაბეჭდეთ მითითებული სტრინგი შიფრაციის შემდეგ

plain = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

text = input("Please, input word: ").upper().split()
number = int(input("Please, input number: "))

if number > 26:
    number = number % 26

def caesar_cipher(t, n):
    caesar = []
    for i in range(len(t)):
        word = ""
        for letter in t[i]:
            index = plain.index(letter) - n
            word += plain[index]
        caesar.append(word)
    return " ".join(caesar)

print(caesar_cipher(text, number))