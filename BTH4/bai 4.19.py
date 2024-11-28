def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Tạo danh sách các số nguyên tố nhỏ hơn 1 triệu
prime_numbers = [i for i in range(1, 1000000) if is_prime(i)]

# Chuyển đổi danh sách thành tuple
P = tuple(prime_numbers)

print("Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu:")
print(P)
