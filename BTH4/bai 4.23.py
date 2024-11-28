def count_letters_and_digits(input_string):
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    return letters, digits

# Nhập câu từ bàn phím
input_string = input("Nhập một câu: ")

# Đếm số chữ cái và chữ số
letters, digits = count_letters_and_digits(input_string)

# In kết quả
print("Số chữ cái:", letters)
print("Số chữ số:", digits)
