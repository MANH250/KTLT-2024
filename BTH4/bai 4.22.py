def is_all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

# Tìm các số trong đoạn từ 1000 đến 3000 mà tất cả các chữ số đều là số chẵn
even_digit_numbers = [num for num in range(1000, 3001) if is_all_even_digits(num)]

# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy
print("Các số có tất cả các chữ số là số chẵn trong đoạn từ 1000 đến 3000 là:")
print(','.join(map(str, even_digit_numbers)))
