# Nhập chuỗi các số nhị phân từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")

# Tách các số nhị phân và kiểm tra xem chúng có chia hết cho 5 không
binary_numbers = input_string.split(',')
divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]

# In các số nhị phân chia hết cho 5
print("Các số nhị phân chia hết cho 5 là:", ','.join(divisible_by_5))
