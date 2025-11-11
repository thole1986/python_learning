import random
import sys


# --------------------------
# Class thường - không tối ưu
# --------------------------
class User:
    def __init__(self, full_name):
        self.full_name = full_name


# --------------------------
# Class Flyweight - tối ưu bộ nhớ
# --------------------------
class User2:
    strings = []  # danh sách từ điển dùng chung cho tất cả user

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.name_indices = [get_or_add(part) for part in full_name.split(" ")]

    def __str__(self):
        return " ".join(self.strings[i] for i in self.name_indices)


# --------------------------
# Tên tiếng Việt phổ biến
# --------------------------
first_names = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan",
    "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"
]

middle_names = [
    "Văn", "Thị", "Hữu", "Minh", "Thanh", "Ngọc", "Xuân",
    "Anh", "Quang", "Tấn"
]

last_names = [
    "An", "Bình", "Cường", "Dũng", "Hà", "Hải", "Hiếu",
    "Hùng", "Khoa", "Khôi", "Long", "Nam", "Phong", "Sơn", "Tú"
]

# --------------------------
# Tạo danh sách người dùng
# --------------------------

def generate_full_name():
    return f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"

N = 100000  # số lượng người dùng

users_normal = [User(generate_full_name()) for _ in range(N)]
users_flyweight = [User2(generate_full_name()) for _ in range(N)]

# --------------------------
# So sánh số lượng chuỗi thực sự lưu
# --------------------------
unique_names_normal = set(u.full_name for u in users_normal)

print("== KẾT QUẢ SO SÁNH ==")
print(f"Tổng số user: {N}")
print(f"Số tên đầy đủ khác nhau (User): {len(unique_names_normal)}")
print(f"Số chuỗi riêng biệt lưu trữ (User): {len(unique_names_normal)}")
print(f"Số từ riêng biệt lưu trữ (User2): {len(User2.strings)}")

# Ước tính bộ nhớ dùng cho danh sách chuỗi
approx_size_user = sum(sys.getsizeof(u.full_name) for u in users_normal)
approx_size_user2 = sum(sys.getsizeof(s) for s in User2.strings)

print(f"Bộ nhớ dùng cho tên (User): ~{approx_size_user} bytes")
print(f"Bộ nhớ dùng cho từ (User2): ~{approx_size_user2} bytes")


"""
    🚀 Gợi ý mở rộng

    Dùng thư viện pympler hoặc tracemalloc để đo chính xác bộ nhớ.

    Áp dụng mô hình Flyweight trong các hệ thống lớn như:

    Hệ thống quản lý nhân sự

    CSDL người dùng

    Game (tên nhân vật)

    Danh sách sản phẩm với thuộc tính lặp lại (màu, hãng...)
"""

class FlyweightFactory:
    """Factory lưu trữ và chia sẻ các đối tượng Flyweight"""
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, value):
        if value not in cls._flyweights:
            cls._flyweights[value] = value
        return cls._flyweights[value]

    @classmethod
    def total_flyweights(cls):
        return len(cls._flyweights)


class Employee:
    def __init__(self, full_name, position, department, location):
        # Tối ưu bằng cách chỉ lưu tham chiếu đến flyweight
        self.full_name = [FlyweightFactory.get_flyweight(part) for part in full_name.split(" ")]
        self.position = FlyweightFactory.get_flyweight(position)
        self.department = FlyweightFactory.get_flyweight(department)
        self.location = FlyweightFactory.get_flyweight(location)

    def __str__(self):
        name = ' '.join(self.full_name)
        return f"{name} | {self.position} | {self.department} | {self.location}"



first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng"]
middle_names = ["Văn", "Thị", "Minh", "Hữu"]
last_names = ["An", "Bình", "Cường", "Dũng", "Hà"]

positions = ["Kỹ sư phần mềm", "Quản lý dự án", "Trưởng phòng nhân sự", "Kế toán"]
departments = ["Kỹ thuật", "Nhân sự", "Tài chính", "Marketing"]
locations = ["Hà Nội", "TP.HCM", "Đà Nẵng"]

# Tạo 10000 nhân viên
employees = []
for _ in range(10000):
    name = f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"
    position = random.choice(positions)
    department = random.choice(departments)
    location = random.choice(locations)
    employees.append(Employee(name, position, department, location))

# In thử
print(employees[0])
print(f"Số Flyweights được sử dụng: {FlyweightFactory.total_flyweights()}")
