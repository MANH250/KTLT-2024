# Sử dụng phương thức 'in'
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("Phần tử 3 có trong danh sách")

# Sử dụng phương thức 'index()'
try:
    index = my_list.index(3)
    print(f"Phần tử 3 có trong danh sách tại vị trí {index}")
except ValueError:
    print("Phần tử 3 không có trong danh sách")
