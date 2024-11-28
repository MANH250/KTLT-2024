# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Loại bỏ tất cả các chữ số khỏi chuỗi
chuoi_moi = ''.join([ky_tu for ky_tu in chuoi if not ky_tu.isdigit()])

# In lại nội dung chuỗi mới
print("Chuỗi mới không có chữ số:", chuoi_moi)
