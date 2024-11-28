def count_upper_lower(input_string):
    upper_count = sum(1 for c in input_string if c.isupper())
    lower_count = sum(1 for c in input_string if c.islower())
    return upper_count, lower_count

# Nhập câu từ bàn phím
input_string = input("Nhập một câu: ")

# Đếm số chữ hoa và chữ thường
upper_count, lower_count = count_upper_lower(input_string)

# In kết quả
print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)
