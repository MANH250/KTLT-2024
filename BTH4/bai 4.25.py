# Nhập danh sách các số từ bàn phím
input_string = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")

# Tách các số và chuyển đổi chúng thành danh sách các số nguyên
numbers = list(map(int, input_string.split(',')))

# Lọc các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# In các số lẻ
print("Các số lẻ là:", ','.join(map(str, odd_numbers)))
