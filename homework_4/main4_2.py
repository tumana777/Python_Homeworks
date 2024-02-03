# დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ტექსტი, ტექსტის სიმბოლოები გადაყავს 
# შესაბამის ASCII სტანდარტში და გვიბეჭდავს ამ რიცხვების თანმიმდევრობას

text = input("Please, input text: ")

for i in text:
    print(f'{i} in "ASCII" standart equals: {ord(i)}')