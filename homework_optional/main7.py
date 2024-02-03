# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს ინტეჯერებისგან შემდგარ ლისტს და 
# გადაამოწმებს ლისტი არის თუ არა მონოტონური, მონოტონური არის იმ შემთხვევაში, თუ ლისტის 
# ყოველი შემდეგი ელემენტი არის მეტი ან ყოველი შემდეგი ელემენტი არის ნაკლები, 
# თუ მონოტონურია უნდა დაგბიბრუნოს პასუხი რომ მონოტონურია და დაგვიწეროს რიცხვები 
# დალაგებულია ზრდადობით თუ კლებადობით, სხვა შემთხვევაში დააბრუნოს რომ ლისტი არ არის მონოტონური.

# ამაზე მარტივად ვერ მოვიფიქრე :)

def monotonous(lst):
    lst1 = []
    lst2 = []
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            lst1.append(True)
        else:
            lst1.append(False)
            
    for i in range(len(lst) - 1):
        if lst[i + 1] < lst[i]:
            lst2.append(True)
        else:
            lst2.append(False)
            
    if all(lst1):
        return "List is monotonous and numbers are sorted ascending"
    elif all(lst2):
        return "List is monotonous and numbers are sorted descending"
    else:
        return "List is not monotonous"
    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 19, 100]
list2 = [100, 50, 25, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list3 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

print(monotonous(list1))
print(monotonous(list2))
print(monotonous(list3))