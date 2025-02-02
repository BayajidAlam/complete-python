class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public Attribute
        self._balance = balance  # Protected Attribute
        self.__pin = "1234"  # Private Attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"${amount} deposited. New balance: ${self._balance}")

    def get_balance(self):
        return self._balance

    def __validate_pin(self, pin):
        return pin == self.__pin  # Private Method

    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"${amount} withdrawn. Remaining balance: ${self._balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid PIN!")

account = BankAccount("Alice", 1000)

# Accessing public member
print(account.account_holder)  # Output: Alice

# Accessing protected member (not recommended)
print(account._balance)  # Output: 1000

# Accessing private member (will cause an error)
# print(account.__pin)  # AttributeError: 'BankAccount' object has no attribute '__pin'


account.deposit(500)  
account.withdraw(200, "1234") 
