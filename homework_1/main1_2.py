# დაწერეთ პროგრამა, რომელიც კითხულობს კუბის გვერდის სიგრძეს (მთელი რიცხვი), გამოითვლის კუბის
# მოცულობას - V და ზედაპირის ფართობს - S და ამ ორ მონაცემს დაბეჭდავს ეკრანზე.

sideLength = int(input("Please input cube side length: "))

cubeVolume = sideLength ** 3
cubeSideArea = sideLength ** 2 * 6

print("Cube volume is: ", cubeVolume)
print("Cube side area is: ", cubeSideArea)