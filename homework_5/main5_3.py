# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2 
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტები

my_list = [43, '22', 12, 66, 210, ["hi"]] 

# Print index of number 210
print(my_list.index(210))

# Add "hello" in last element of my_list
my_list[-1].append("hello")

# Remove 2nd indexed element in my_list
my_list.pop(2)
print(my_list)

# Copy my_list
my_list_2 = my_list.copy()
my_list_2.clear()

print(my_list, my_list_2, sep="\n")