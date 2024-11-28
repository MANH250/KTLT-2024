def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def find_abundant_numbers(n):
    abundant_numbers = []
    for i in range(1, n):
        if sum_of_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))

# Tìm và in các số nguyên dương nhỏ hơn n có tổng các ước số lớn hơn chính nó
abundant_numbers = find_abundant_numbers(n)
print("Các số nguyên dương nhỏ hơn", n, "có tổng các ước số lớn hơn chính nó là:")
for num in abundant_numbers:
    print(num)
