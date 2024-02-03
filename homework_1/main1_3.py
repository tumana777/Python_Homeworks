# დაწერეთ პროგრამა, რომელიც ცალ-ცალკე კითხულობს კომპიუტერის შემადგენელი ნაწილების ფასებს -
# მონიტორის, სისტემური ბლოკის, კლავიატურის და მაუსის. ამ მონაცემების გამოყენებით გამოითვლის
# კომპიუტერის ფასს და დაბეჭდავს ეკრანზე.

screenPrice = float(input("Please input screen price: "))
casePrice = float(input("Please input case price: "))
keyboardPrice = float(input("Please input keyboard price: "))
mousePrice = float(input("Please input mouse price: "))

computerPrice = screenPrice + casePrice + keyboardPrice + mousePrice

print("PC price is: ", computerPrice)