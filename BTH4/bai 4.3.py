# Nhập chuỗi từ người dùng
S = input("Nhập chuỗi S: ")

# In từng ký tự của chuỗi, mỗi ký tự trên một dòng và ở dạng in hoa
for char in S:
    if char not in [' ', '\t']:  # Bỏ qua dấu cách và dấu tab
        print(char.upper())
