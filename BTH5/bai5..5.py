print(" Hồ Hữu Mạnh ")
print("MSSV: 235752021610035")
# File: main.py
import mymath

# Nhập số lượng và giá trị của danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử của danh sách: "))
numbers = []
for _ in range(n):
    number = int(input("Nhập một số: "))
    numbers.append(number)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = mymath.find_max(numbers)
min_value = mymath.find_min(numbers)

# In kết quả
print("Phần tử lớn nhất trong danh sách là:", max_value)
print("Phần tử nhỏ nhất trong danh sách là:", min_value)
