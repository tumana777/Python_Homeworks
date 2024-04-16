from bank_account import BankAccount
import unittest

class TestBank(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount(1, "Account1", 500)
        self.account2 = BankAccount(2, "Account2")
    
    def test_deposit(self):
        self.assertEqual(self.account1.deposit(100), "Deposited $100. New balance: $600")
        self.assertEqual(self.account1.deposit(1000), "Deposited $1000. New balance: $1600")
        self.assertEqual(self.account2.deposit(300), "Deposited $300. New balance: $300")
        self.assertEqual(self.account1.deposit(0), "Invalid amount for deposit.")
        self.assertEqual(self.account2.deposit(-100), "Invalid amount for deposit.")

    def test_withdraw(self):
        self.assertEqual(self.account1.withdraw(200), "Withdrew $200. New balance: $300")
        self.assertEqual(self.account2.withdraw(0), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account2.withdraw(-500), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.account1.withdraw(300), "Withdrew $300. New balance: $0")
        self.assertEqual(self.account1.withdraw(10), "Insufficient funds or invalid amount for withdrawal.")

    def test_balance(self):
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 0)

if __name__ == "__main__":
    unittest.main()