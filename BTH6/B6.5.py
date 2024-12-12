print("Ho Huu Manh")
print("Msv:235752021610035")
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ' '.join(self.text.split()[::-1])

# Ví dụ sử dụng
reverser = ReverseWords('hello .py')
print("Chuỗi đảo ngược:", reverser.reverse())
