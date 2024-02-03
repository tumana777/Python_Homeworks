# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრინგს და შეამოწმებს არის თუ არა სტრიქონი ანაგრამი


def main():
    str1 = input("Please, input string 1: ")
    str2 = input("Please, input string 2: ")
    if anagram_checker(str1, str2):
        print(f"{str1} and {str2} are anagrams!")
    else:
        print(f"{str1} and {str2} are not anagrams!")

def anagram_checker(word1, word2):
    
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False
            
main()
