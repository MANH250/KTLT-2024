# Nhập chuỗi từ bàn phím
input_string = input("Nhập các từ tiếng Anh tách nhau bởi dấu cách: ")

# Tách các từ và sắp xếp theo thứ tự từ điển
words = input_string.split()
words.sort()

# In các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
