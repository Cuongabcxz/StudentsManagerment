import math
from main.student import Student


class StudentsManager:

    list_student = []

    # Hàm tạo ID tăng dần cho nhân viên
    def generateID(self):
        max_id = 1
        if self.count_student() > 0:
            max_id = self.list_student[0].get_id()
            for student in self.list_student:
                if max_id < student.get_id():
                    max_id = student.get_id()
            max_id = max_id + 1
        return max_id

    def count_student(self):
        return self.list_student.__len__()

    def add_student(self):
        # Khởi tạo một sinh viên mới
        my_id = self.generateID()
        name = input("Nap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        sc_math = float(input("Nhap diem toan: "))
        sc_physical = float(input("Nhap diem Ly: "))
        sc_chemistry = float(input("Nhap diem Hoa: "))
        student = Student(my_id, name, sex, age, sc_math,
                          sc_physical, sc_chemistry)
        self.cal_sc_average(student)
        self.set_rank(student)
        self.list_student.append(student)

    def update_student(self, my_id):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        student: Student = self.findByID(my_id)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if student is not None:
            # nhập thông tin sinh viên
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            sc_math = float(input("Nhap diem toan: "))
            sc_physical = float(input("Nhap diem Ly: "))
            sc_chemistry = float(input("Nhap diem Hoa: "))
            # cập nhật thông tin sinh viên
            student.set_name(name)
            student.set_sex(sex)
            student.set_age(age)
            student.set_sc_math(sc_math)
            student.set_sc_physical(sc_physical)
            student.set_sc_chemistry(sc_chemistry)
            self.cal_sc_average(student)
            self.set_rank(student)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(my_id))

    # Hàm sắp xếp danh sach sinh vien theo ID tăng dần
    def sortByID(self):
        self.list_student.sort(key=lambda x: x.get_id(), reverse=False)

    # Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.list_student.sort(key=lambda x: x.get_name(), reverse=False)

    # Hàm sắp xếp danh sach sinh vien theo điểm TB tăng dần
    def sortBy_sc_average(self):
        self.list_student.sort(key=lambda x: x.get_sc_average(), reverse=False)

        # Hàm tính điểm TB cho sinh viên

    def cal_sc_average(self, student: Student):
        sc_average = (student.get_sc_math() + student.get_sc_physical()
                      + student.get_sc_chemistry()) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        student.set_sc_average(math.ceil(sc_average * 100) / 100)

    # Hàm tìm kiếm sinh viên theo ID
    # Trả về một sinh viên
    def findByID(self, ID):
        searchResult = None
        if self.count_student() > 0:
            for student in self.list_student:
                if student.get_id() == ID:
                    searchResult = student
        return searchResult

    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if self.count_student() > 0:
            for student in self.list_student:
                if keyword.upper() in student.get_name().upper():
                    listSV.append(student)
        return listSV

    # Hàm xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        st = self.findByID(ID)
        if st is not None:
            self.list_student.remove(st)
            isDeleted = True
        return isDeleted

    # Hàm xếp loại học lực cho nhân viên
    def set_rank(self, student: Student):
        if student.get_sc_average() >= 8:
            student._rank = "Gioi"
        elif student.get_sc_average() >= 6.5:
            student._rank = "Kha"
        elif student.get_sc_average() >= 5:
            student._rank = "Trung Binh"
        else:
            student._hocLuc = "Yeu"

        # Hàm hiển thị danh sách sinh viên ra màn hình console

    def display_student(self, list_student):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} "
              "{:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan",
                      "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if list_student.__len__() > 0:
            for st in list_student:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} "
                      "{:<8} {:<8} {:<8} {:<8}"
                      .format(st.get_id(), st.get_name(),
                              st.get_sex(), st.get_age(),
                              st.get_sc_math(), st.get_sc_physical(),
                              st.get_sc_chemistry(), st.get_sc_average(),
                              st.get_rank()))
        print("\n")

        # Hàm trả về danh sách sinh viên hiện tại

    def get_list_student(self):
        return self.list_student
    
    def print_Hello():
        return "Hello world"
