import numpy as np
print("Ho Huu Manh")
print("Msv:235752021610035")
# Định nghĩa kiểu dữ liệu của các trường
student_dtype = np.dtype([
    ('name', 'U20'),     # Tên sinh viên là chuỗi có tối đa 20 ký tự
    ('height', 'f8'),    # Chiều cao là số thực (float64)
    ('class', 'i4')      # Lớp là số nguyên (int32)
])

# Tạo mảng với dữ liệu sinh viên
students = np.array([
    ('Alice', 1.65, 10),
    ('Bob', 1.80, 11),
    ('Charlie', 1.70, 10),
    ('David', 1.75, 12),
    ('Eve', 1.60, 11),
    ('Frank', 1.85, 10)
], dtype=student_dtype)

print("Original array:")
print(students)

# Sắp xếp mảng theo lớp và chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

print("\nArray sorted by class and height:")
print(sorted_students)
