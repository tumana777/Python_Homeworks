# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით, 
# როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები. 
# შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.

def main():
    
    # Create BankAccount Class
    class BankAccount:
        # Initilize Attributes
        def __init__(self, acc_num, acc_holder, balance):
            self.acc_num = acc_num
            self.acc_holder = acc_holder
            self.balance = balance
        # Deposit Method
        def deposit(self):
            amount = int(input('Please input deposit amount: '))
            self.balance += amount
            self.balanceAmount()
        # Withdraw Method
        def withdraw(self):
            amount = int(input('Please input withdraw amount: '))
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Insufficient amount!')
            self.balanceAmount()
        # Return Balance
        def balanceAmount(self):
            print(f'Dear {self.acc_holder}, your balance is: ${self.balance:0,.0f}')
        
    # User input for deposit or withdraw
    def dep_or_withdraw(account):
        text = input('Please input "d" for deposit, "w" for withdraw: ')
        if text == 'd':
            return account.deposit()
        elif text == 'w':
            return account.withdraw()
        else:
            return account.balanceAmount()
    
    # Create several objects
    account1 = BankAccount(1, 'tumana111', 1000)
    account2 = BankAccount(2, 'tumana222', 2000)
    account3 = BankAccount(3, 'tumana333', 3000)
    
    # Call objects methods 
    dep_or_withdraw(account1)
    dep_or_withdraw(account2)
    dep_or_withdraw(account3)

main()