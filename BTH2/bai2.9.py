# Nhập chuỗi từ bàn phím
str_input = input("Enter a string: ")

# Khởi tạo từ điển để lưu số lần xuất hiện của các ký tự
char_count = {}

# Duyệt qua từng ký tự trong chuỗi
for char in str_input:
    if char in char_count:
        char_count[char] += 1  # Nếu ký tự đã có trong từ điển, tăng số đếm lên 1
    else:
        char_count[char] = 1  # Nếu chưa có, thêm vào từ điển với giá trị 1

# In kết quả
print(char_count)
