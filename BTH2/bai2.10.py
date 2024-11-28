# Nhập xâu ký tự từ người dùng
string_input = input("Nhập xâu ký tự: ")

# Sử dụng phương thức split để tách xâu thành danh sách các từ
words = string_input.split()

# In ra danh sách các từ
print("Danh sách các từ:", words)

# Sử dụng phương thức join để nối lại các từ thành xâu ký tự, cách nhau bởi dấu cách
joined_string = ' '.join(words)

# In ra xâu ký tự đã nối lại
print("Xâu ký tự sau khi nối lại:", joined_string)
