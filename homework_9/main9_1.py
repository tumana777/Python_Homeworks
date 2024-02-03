# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით დაგენერირებული 
# ელემენტისგან შემდგარ ლისტს, გამოიყენეთ sort() მეთოდი და sorted() ფუნქცია, დააბრუნეთ 
# დასორტირებული ლისტი ჯერ ზრდადობით და შემდეგ კლებადობით

from random import randint

def sorterBySort():
    
    randList = [randint(-200, 200) for i in range(100)]
    
    def sortedList(arr):
        arr.sort()
        return arr
    
    def reverseSortList(arr):
        arr.sort(reverse=True)
        return arr
    
    print(f"\nThis list is sorted ascending: \n\n{sortedList(randList)}")
    print(f"\nThis list is sorted descending: \n\n{reverseSortList(randList)}")
    
def sorterBySorted():
    
    randList = [randint(-200, 200) for i in range(100)]
    
    def sortedList(arr):
        return(sorted(arr))
    
    def reverseSortList(arr):
        return(sorted(arr, reverse=True))
    
    print(f"\nThis list is sorted ascending: \n\n{sortedList(randList)}")
    print(f"\nThis list is sorted descending: \n\n{reverseSortList(randList)}")

sorterBySort()
sorterBySorted()
