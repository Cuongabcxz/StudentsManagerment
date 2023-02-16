from main.students_managerment import StudentsManager

if __name__ == '__main__':
    # khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
    student_manager = StudentsManager()
    while 1 == 1:
        print("\nCHUONG TRINH QUAN LY SINH VIEN Python")
        print("*************************MENU**************************")
        print("**  1. Them sinh vien.                               **")
        print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
        print("**  3. Xoa sinh vien boi ID.                         **")
        print("**  4. Tim kiem sinh vien theo ten.                  **")
        print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
        print("**  6. Sap xep sinh vien theo ten.                   **")
        print("**  7. Sap xep sinh vien theo ID.                    **")
        print("**  8. Hien thi danh sach sinh vien.                 **")
        print("**  0. Thoat                                         **")
        print("*******************************************************")
        print("Hello world")

        key = int(input("Nhap tuy chon: "))
        if key == 1:
            print("\n1. Them sinh vien.")
            student_manager.add_student()
            print("\nThem sinh vien thanh cong!")
        elif key == 2:
            if student_manager.count_student() > 0:
                print("\n2. Cap nhat thong tin sinh vien. ")
                print("\nNhap ID: ")
                ID = int(input())
                student_manager.update_student(ID)
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 3:
            if student_manager.count_student() > 0:
                print("\n3. Xoa sinh vien.")
                print("\nNhap ID: ")
                ID = int(input())
                if student_manager.deleteById(ID):
                    print("\nSinh vien co id = ", ID, " da bi xoa.")
                else:
                    print("\nSinh vien co id = ", ID, " khong ton tai.")
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 4:
            if student_manager.count_student() > 0:
                print("\n4. Tim kiem sinh vien theo ten.")
                print("\nNhap ten de tim kiem: ")
                name = input()
                searchResult = student_manager.findByName(name)
                student_manager.display_student(searchResult)
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 5:
            if student_manager.count_student() > 0:
                print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
                student_manager.sortBy_sc_average()
                student_manager.display_student(student_manager.get_list_student())
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 6:
            if student_manager.count_student() > 0:
                print("\n6. Sap xep sinh vien theo ten.")
                student_manager.sortByName()
                student_manager.display_student(student_manager.get_list_student())
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 7:
            if student_manager.count_student() > 0:
                print("\n6. Sap xep sinh vien theo ID.")
                student_manager.sortByID()
                student_manager.display_student(student_manager.get_list_student())
            else:
                print("\nSanh sach sinh vien trong!")
        elif key == 8:
            if student_manager.count_student() > 0:
                print("\n7. Hien thi danh sach sinh vien.")
                student_manager.display_student(student_manager.get_list_student())
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 0:
            print("\nBan da chon thoat chuong trinh!")
            break
        else:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")