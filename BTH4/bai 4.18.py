def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Nhập số nguyên n từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Tạo danh sách các số Fibonacci nhỏ hơn n và in ra màn hình
fib_list = fibonacci(n)
print("Các số Fibonacci nhỏ hơn", n, "là:")
for num in fib_list:
    print(num)
