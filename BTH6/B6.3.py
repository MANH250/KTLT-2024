print("Ho Huu Manh")
print("Msv:235752021610035")
class Nguoi:
    def getGender(self):
        pass

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Ví dụ sử dụng
male = Nam()
female = Nu()
print("Giới tính:", male.getGender())
print("Giới tính:", female.getGender())