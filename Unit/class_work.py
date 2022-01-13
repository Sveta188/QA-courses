import random
from string import ascii_lowercase as string
sub = {'p.e': None, 'math': None, 'literature': None, 'geography': None, 'biology': None}


class Student:
    def __init__(self, first_name, initials, group_num, marks):
        self.first_name = first_name
        self.initials = initials
        self.group_num = group_num
        self.marks = marks

    def __repr__(self):
        return f"{self.first_name}, {self.initials}, {self.group_num}, {self.marks}"


class School:
    def __init__(self):
        self.school_class = dict()

    def group(self, group_name):
        self.school_class.update({str(group_name): set()})

    def add_student(self, student):
        self.school_class[str(student.group_num)].update({student})

    def students_5_6(self):

        for group_name in self.school_class:
            for student in self.school_class[group_name]:
                average = sum(student.marks.values()) / 5

                if 5 <= average <= 6:
                    print(f'Студент {student.first_name} {student.initials} имеет средний бал равный {average}!')

    def get_mates(self, group_num):
        li = list()
        group_num = str(group_num)
        students_group = self.school_class[group_num]
        if students_group:
            print(f'Студент(ы) группы №{group_num}')
            for student in students_group:
                print(student.first_name, student.initials)
        else:
            print(f'Группа №{group_num} пуста!')

    def average_7(self):
        for group_name in self.school_class:
            for student in self.school_class[group_name]:
                average = sum(student.marks.values()) / 5

                if average >= 7:
                    print(f'Студент {student.first_name} {student.initials} имеет средний бал равный {average}!')

