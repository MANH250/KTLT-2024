# Giả sử ds là danh sách đã nhập từ bàn phím
ds = input('Nhập chuỗi: ').split()

# Bỏ phần tử '123' khỏi danh sách
if '123' in ds:
    ds.remove('123')

# In từng phần tử trong danh sách ds
for ch in ds:
    print(ch)
