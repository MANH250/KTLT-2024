# Nhập vào khoảng (a, b)
a = int(input("Enter the lower bound (a): "))
b = int(input("Enter the upper bound (b): "))

# Duyệt qua từng số trong khoảng (a, b)
for number in range(a, b + 1):
    # Tính số nghịch đảo
    reversed_number = str(number)[::-1]
    # Tính giá trị dưới dạng thập phân
    decimal_value = float(number)

    print(f"Number: {number}, Reversed: {reversed_number}, Decimal: {decimal_value}")
