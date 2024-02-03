# დაწერეთ ფუნქცია, რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით დაგენერირებული 
# ელემენტისგან შემდგარ ლისტს, გამოიყენეთ ორი სორტირების ალგორითმი(არ აქვს არსებითი 
# მნიშვნელობა, რომელი ალგორითმები იქნება), ერთი ალგორითმით დაასორტირეთ ზრდადობით, 
# მეორე ალგორითმით დაასორტირეთ კლებადობით, ორივე შედეგი დაპრინტეთ ტერმინალში. 

from random import randint

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        
    leftList = []
    rightList = []
        
    for num in arr:
        if num < pivot:
            leftList.append(num)
        else:
            rightList.append(num)
            
    return quickSort(leftList) + [pivot] + quickSort(rightList)

def insertion_sort(arr):
    indexing_length = range(1, len(arr))
    for i in indexing_length:
        value_to_sort = arr[i]
        while arr[i-1] < value_to_sort and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr

def sorter():
    randList = [randint(-200, 200) for i in range(100)]
    
    print(f"\nThis list is sorted ascending: \n\n{quickSort(randList)}")
    print(f"\nThis list is sorted descending: \n\n{insertion_sort(randList)}")
    
sorter()