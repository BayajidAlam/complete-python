class Account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc
  
  def debit(self,amount):
    self.balance -= amount
    print(amount ,"was debited")
    print("Current balance: ", self.get_balance())

  def credit(self, amount):
    self.balance += amount
    print(amount ,"was credited")
    print("Current balance: ", self.get_balance())
  
  def get_balance(self):
    return self.balance

myaccount = Account(1000, 123456)
myaccount.credit(500)
myaccount.debit(200)  
