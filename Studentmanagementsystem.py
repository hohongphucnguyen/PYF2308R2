class student:
    def __init__(self, masv, ho_ten, ngay_sinh, que_quan, chuyen_nganh, lop):
        self.masv = masv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan
        self.chuyen_nganh = chuyen_nganh
        self.lop = lop
    def __str__(self):
        
class Student_List:
    def __init__(self, student_list):
        self.student_list = student_list
    def display(self):
        for student in Student_List:
            print(student)
    def add_student(self,student);
        self.student_list.append(student)
    def update_student(self, student):
        pass
    def search(self, keyword):
        pass
    def delete_student(self, keyword):
        pass