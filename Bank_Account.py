class BankAccount(object):
  balance = 0

  def __init__(self, name):
    self.name = name


  def __repr__(self):
    return "%s's account Balance: $%.2f" % (self.name, self.balance)


  def show_balance(self):
    print "%s's account Balance: $%.2f" % (self.name, self.balance)

  def deposit(self, amount):
    self.amount = amount
    if self.amount <= 0:
      print "Please enter an amount higher than 0."
      return
    else:
      print "$%.2f has been added to your account" % (self.amount)
      self.balance += amount
      self.show_balance()

  def withdraw(self, amount):
    self.amount = amount
    if amount > self.balance:
      print "You can not with draw that amount"
    else:
      return "$%.2f has been withdrawn from your account" % (self.amount)
    self.balance -= amount
    self.show_balance()

my_account = BankAccount("luke")
my_account.deposit(2000)

my_account.withdraw(1000)


