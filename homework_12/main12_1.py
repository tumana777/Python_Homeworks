# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება, პროგრამას 
# დააბეჭდინეთ დიქტის სახით რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში

# input: The wind howled and howled all night long

# output: {“the”: 1, “wind”:1, “howled”:2, “and”:1, “all”:1, ”night”:1, “long”:1}

def text_to_dict(text):

    words = text.lower().split()

    return {word : words.count(word) for word in words}

userText = input("Please, input any text: ")

print(text_to_dict(userText))