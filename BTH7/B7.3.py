print("Ho Huu Manh")
print("Msv:235752021610035")
def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

# Ví dụ sử dụng
read_entire_file('file.txt')  # Thay 'file.txt' bằng tên file của bạn