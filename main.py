from bank_acc import *
member1 = BankAccount("rawda" , 1000)
member2 = BankAccount("rasha" , 5000)

member1.deposite(200)

member1.withdraw(15000)

member1.withdraw(500)

member1.transfer(member2 , 100)

member3 = RewardsAcct("barakat", 3000)

member3.get_balance()

member3.deposite(100)

member3.transfer(100, member2)

member4 = SavingsAcct("eman", 1000)

member4.get_balance()

member4.deposite(100)

member4.transfer(member1, 1000)
member4.transfer(member2, 1000)
