# Giả sử ds là danh sách đã nhập từ bàn phím
ds = input('Nhập chuỗi: ').split()

# Lấy danh sách nhưng bỏ phần tử đầu và cuối
x = ds[1:-1]

# In từng phần tử trong danh sách x
for c in x:
    print(c)
