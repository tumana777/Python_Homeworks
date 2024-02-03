# დაწერეთ თამაში ჯეირანი

# for quick input, you can also input number 1, 2 or 3. Where 
# 1 equls "stone", 2 equals "scissors" and 3 equals "paper"

from random import randint

while True:
    player = input("Please, input action: ")
    ai = randint(1, 3)
    
    if player == "stone" or player == "1":
        if ai == 3:
            print("Your action is 'stone' and ai's action is 'paper', so you Lost!")
            break
        elif ai == 2:
            print("Your action is 'stone' and ai's action is 'scissors', so you Win!")
            break
        else:
            print("Your and ai's actions are 'stone', so there is a draw and try again!")
    elif player == "scissors" or player == "2":
        if ai == 3:
            print("Your action is 'scissors' and ai's action is 'paper', so you Win!")
            break
        elif ai == 1:
            print("Your action is 'scissors' and ai's action is 'stone', so you Lost!")
            break
        else:
            print("Your and ai's actions are 'scissors', so there is a draw and try again!")
    elif player == "paper" or player == "3":
        if ai == 2:
            print("Your action is 'paper' and ai's action is 'scissors', so you Lost!")
            break
        elif ai == 1:
            print("Your action is 'paper' and ai's action is 'stone', so you Win!")
            break
        else:
            print("Your and ai's actions are 'paper', so there is a draw and try again!")
    else:
        print("Please, input correct action!")