# Khởi tạo các biến
a, b = 1, 2
total = 0

# In dãy Fibonacci và tính tổng số chẵn
print("Dãy số Fibonacci:")
while a < 4000000:
    print(a, end=" ")
    
    # Kiểm tra xem số a có phải là số chẵn không
    if a % 2 == 0:
        total += a
    
    # Cập nhật giá trị của a và b
    a, b = b, a + b

print("\nTổng các số chẵn trong dãy Fibonacci là:", total)
