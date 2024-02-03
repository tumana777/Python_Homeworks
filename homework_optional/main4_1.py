# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს შეაყვანინებს წელს და დაგვიბეჭდავს ეს ნაკიანი წელი არის თუ არა

year = int(input("Please, input year: "))

print(f"{year} is Leap year") if year % 4 == 0 else print(f"{year} is not Leap year")