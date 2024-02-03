# დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს “small”, “tall”, “middle”
# a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაბეჭდეთ პირველივე 	სიტყვა რაც აღმოჩნდება ტექსტში
# b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ, რომ ტექსტში ეს 	სამი სიტყვა არ მოიძებნა

text = input("Please, input some text: ")

word1 = "small"
word2 = "tall"
word3 = "middle"

if word1 in text:
    print(f"{word1} is in your text :)")
elif word2 in text:
    print(f"{word2} is in your text :)")
elif word3 in text:
    print(f"{word3} is in your text :)")
else:
    print("There is no this three words in your text")