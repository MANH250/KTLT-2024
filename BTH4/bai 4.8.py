# Nhập dãy các từ từ bàn phím
chuoi = input("Nhập một dãy các từ: ")

# Tách các từ trong chuỗi
tu = chuoi.split()

# Tìm độ dài của từ dài nhất
do_dai_max = max(len(t) for t in tu)

# Tìm tất cả các từ có độ dài bằng độ dài lớn nhất
tu_dai_nhat = [t for t in tu nêu len(t) == do_dai_max]

# In ra các từ dài nhất
print("Từ dài nhất:", tu_dai_nhat)
