print("Ho Huu Manh")
print("Msv:235752021610035")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Số dư hiện tại:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Rút tiền:", amount)
        else:
            print("Không đủ tiền trong tài khoản.")

    def check_balance(self):
        print("Số dư hiện tại:", self.balance)

# Ví dụ sử dụng
atm = ATM(1000)
atm.check_balance()
atm.deposit(500)
atm.withdraw(200)
atm.check_balance()
