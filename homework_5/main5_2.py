# შექმენით ცარიელი ლისტი, რომელსაც შეავსებთ შემთხვევითი რიცხვებით, დაბეჭდეთ ელემენტებიდან 
# მინიმალური და მაქსიმალური მნიშვნელობები

# This program prints minimum and maximum value of list

import random
mylist = []

# Add mylist 15 random numbers between -200 and 200
for num in range(15):
    mylist.append(random.randint(-200, 200))

print(mylist)

# Determine minimum and maximum values from mylist without built-in min and max functions
new_min = mylist[0]

for num in mylist:
    if num < new_min:
        new_min = num

new_max = mylist[0]

for num in mylist:
    if num > new_max:
        new_max = num

print(new_min)
print(new_max)

# Determine minimum and maximum values from mylist by built-in min and max functions
print(min(mylist))
print(max(mylist))
