# Yêu cầu người dùng nhập vào số nguyên n
n = int(input("Nhập vào một số: "))

# Tạo dictionary với các cặp (i, i*i)
d = {i: i * i for i in range(1, n + 1)}

# In ra dictionary
print(d)
