from datetime import datetime


class Address:
    def __init__(self, country, state, city, street, postal):
        self.country = country
        self.state = state
        self.city = city
        self.street = street
        self.postal_code = postal


class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise NameError("Invalid Address from person class...")

            self.addresses = address
        else:
            raise NameError("Invalid Address from person class1...")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise NameError("Invalid Address from person class2...")

        self.addresses.append(address)


class Student(Person):
    def __init__(self, first, last, dob, phone, address, international=False):
        super().__init__(first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise NameError("Invalid Enroll...")

        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3


class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        super().__init__(self, first, last, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raised = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raised:
            self.salary += 20000
            self.got_raised = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise NameError("Invalid Course...")

        self.courses.append(course)


class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max_ = max_
        self.min_ = min_
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise NameError("Invalid Professor...")
            self.professors = professor
        else:
            raise NameError("Invalid Professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise NameError("Invalid Professor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise NameError("Invalid Enroll...")

        if len(self.enrollments) == self.max_:
            raise NameError("Cannot Enroll, Course is Full...")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min_


class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise NameError("Invalid Student...")

        if not isinstance(course, Course):
            raise NameError("Invalid Course...")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade


def main():
    # Prompt the user for address information
    country = input("Enter the country: ")
    state = input("Enter the state: ")
    city = input("Enter the city: ")
    street = input("Enter the street: ")
    postal_code = input("Enter the postal code: ")

    # Create an instance of the Address class
    address = Address(country, state, city, street, postal_code)

    # Prompt the user for person information
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    date_of_birth = input("Enter the date of birth (MM-DD-YYYY): ")
    phone = input("Enter the phone number: ")

    # Create an instance of the Person class
    person = Person(first_name, last_name, date_of_birth, phone, address)

    # Prompt the user for student information
    international = input("Is the student an international student? (yes/no): ")
    if international.lower() == "yes":
        international = True
    else:
        international = False
    # Create an instance of the Student class
    student = Student(first_name, last_name, date_of_birth, phone, address, international)

    # professor
    prof_fname = input("Enter Professor First Name: ")
    prof_lname = input("Enter Professor Last Name: ")
    date_of_birth = input("Enter the date of birth (MM-DD-YYYY): ")
    phone = input("Enter the phone number: ")
    salary = 15000

    professor = Professor(prof_fname, prof_lname, date_of_birth, phone, address, salary)

    # Course
    course_name = input("Enter Your Course Name: ")
    course_code = input("Enter Course Code: ")
    course_max_ = 3
    course_min_ = 1

    course = Course(course_name, course_code, course_max_, course_min_, professor)

    # Print the student's first and last name
    print(student.first_name, student.last_name)

    # Print the student's date of birth
    print(student.date_of_birth)

    # Print whether the student is an international student
    print("International Student: ", student.international)


if __name__ == "__main__":
    main()

