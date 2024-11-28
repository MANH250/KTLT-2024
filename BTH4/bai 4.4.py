# Nhập danh sách từ người dùng, các phần tử cách nhau bởi dấu trống hoặc tab
input_string = input("Nhập danh sách các phần tử, cách nhau bởi dấu trống hoặc tab: ")

# Sử dụng phương thức split() để tách các phần tử trong chuỗi
elements = input_string.split()

# In ra danh sách các phần tử
print("Danh sách các phần tử vừa nhập:")
for element in elements:
    print(element)
