import re

def kiem_tra_mat_khau():
    value = []
    items = [x for x in input("Nhập mật khẩu: ").split(',')]
    for p in items:
        if len(p) < 6 or len(p) > 12:
            continue
        if not re.search("[a-z]", p):
            continue
        if not re.search("[0-9]", p):
            continue
        if not re.search("[A-Z]", p):
            continue
        if not re.search("[$#@]", p):
            continue
        if re.search("\s", p):
            continue
        value.append(p)
    return ",".join(value)

# Gọi hàm và in kết quả
print(kiem_tra_mat_khau())
