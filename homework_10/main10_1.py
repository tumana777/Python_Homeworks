# დაწერეთ პითონის ფუნქცია რომელიც დააგენერირებს 100 შემთხვევითობის პრინციპით არჩეული რიცხვებით შევსებულ ლისტს.
# დაწერეთ ფუნქცია, რომელიც ხაზობრივი ძიების გამოყენებით მოიძიებს მოცემულ ლისტში რომელიმე ელემენტს.
# გამოიყენეთ სორტირების ერთ-ერთი ალგორითმი და დასორტირებულ სიაში ელემენტის ძიებისთვის დაწერეთ ბინარული ძიება.

from random import randint

def randNums(from_, to, qty=100):
    
    return [randint(from_, to) for _ in range(qty)]

def linear_search(arr, n):
    
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

def binary_search(arr, value):
    
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            return mid
        
    return -1

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

lst = randNums(-200, 200)

print(lst)

result = linear_search(lst, 5)

print(f"\nYour number in list is at index {result}\n")

sortedList = quickSort(lst)

print(sortedList)

result = binary_search(sortedList, 5)

print(f"\nYour number in list is at index {result}\n")