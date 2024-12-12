print("Ho Huu Manh")
print("Msv:235752021610035")
import math  # Đảm bảo thư viện math được nhập khẩu

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

# Ví dụ sử dụng
circle = Circle(5)
print("Diện tích:", circle.area())
print("Chu vi:", circle.circumference())
