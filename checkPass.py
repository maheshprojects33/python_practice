class Student:
    def __init__(self, name, code, marks_eng, marks_math, marks_science, marks_nepali):
        self.name = name
        self.code = code
        self.marks_eng = marks_eng
        self.marks_math = marks_math
        self.marks_science = marks_science
        self.marks_nepali = marks_nepali

    def get_total_marks(self):
        total_marks = int(self.marks_eng) + int(self.marks_math) + int(self.marks_science) + int(self.marks_nepali)
        print(f"Your Total Marks: {total_marks}")
        return total_marks

    def get_avg_marks(self):
        total_marks = self.get_total_marks()
        avg_marks = total_marks /4
        print(f"Your Average Marks: {avg_marks}")

    def get_sub_list(self):
        sub_list = [self.marks_eng, self.marks_math, self.marks_science, self.marks_nepali]
        return sub_list

    def get_result(self):
        sub_list = self.get_sub_list()
        print(sub_list)

        if int(self.marks_eng) < 40 or int(self.marks_math) < 40 or int(self.marks_science) < 40 or int(self.marks_nepali) < 40:
            print("Fail | ")
        else:
            print("Pass")


    def get_percentage(self):
        pass


if __name__ == "__main__":
    name = input("Enter Your Name: ")
    code = input("Enter Your Code: ")
    marks_eng = input("Enter Your Marks in English: ")
    marks_math = input("Enter Your Marks in Math: ")
    marks_science = input("Enter Your Marks in Science: ")
    marks_nepali = input("Enter Your Marks in Nepali: ")
    student = Student(name, code, marks_eng, marks_math, marks_science, marks_nepali)
    student.get_total_marks()
    student.get_avg_marks()
    student.get_result()




# student = Student("name", "code", "marks_eng", "marks_math", "marks_science", "marks_nepali")
# # student.name = input(f"Enter Your Name: ")
# # student.code = input(f"Enter Your Code: ")
# student.marks_eng = input(f"Enter Your Marks in English: ")
# student.marks_math = input(f"Enter Your Marks in Math: ")
# student.marks_science = input(f"Enter Your Marks in Science: ")
# student.marks_nepali = input(f"Enter Your Marks in Nepali: ")
#
# student.get_result()