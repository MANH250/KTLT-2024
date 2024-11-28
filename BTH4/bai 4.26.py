def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        type, amount = transaction.split()
        amount = int(amount)
        if type == 'D':
            balance += amount
        elif type == 'W':
            balance -= amount
    return balance

# Nhập nhật ký giao dịch từ bàn phím
transactions = []
while True:
    transaction = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
    if not transaction:
        break
    transactions.append(transaction)

# Tính số tiền thực của tài khoản
balance = calculate_balance(transactions)
print("Số tiền thực của tài khoản là:", balance)
