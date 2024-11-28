import math

def giai_phuong_trinh_bac_hai(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    
    # Kiểm tra giá trị của delta để xác định số nghiệm
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

# Nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm và in kết quả
ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
print(ket_qua)
