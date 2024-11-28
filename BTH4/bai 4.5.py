# Nhập danh sách các từ từ người dùng, cách nhau bởi dấu trống hoặc tab
input_string = input("Nhập danh sách các từ, cách nhau bởi dấu trống hoặc tab: ")

# Sử dụng phương thức split() để tách các từ trong chuỗi
words = input_string.split()

# Đảo ngược thứ tự các từ
reversed_words = words[::-1]

# In ra các từ theo thứ tự ngược lại
print("Các từ theo thứ tự ngược lại:")
print(" ".join(reversed_words))
