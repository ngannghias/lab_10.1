class Student:
    def __init__(self, ten, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def print_diemtk(self):
        diem_tk = (self.diem_toan + self.diem_ly + self.diem_hoa) / 3
        print(f"Điểm tổng kết của {self.ten}: {diem_tk}")

# Nhập thông tin từ người dùng
ten_sv = input("Nhập tên sinh viên: ")
diem_toan_sv = float(input("Nhập điểm Toán: "))
diem_ly_sv = float(input("Nhập điểm Lý: "))
diem_hoa_sv = float(input("Nhập điểm Hóa: "))

# Tạo một đối tượng sinh viên
sinh_vien = Student(ten_sv, diem_toan_sv, diem_ly_sv, diem_hoa_sv)

# In ra điểm tổng kết của sinh viên
sinh_vien.print_diemtk()
