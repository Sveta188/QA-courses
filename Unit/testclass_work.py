import unittest
from class_work import School, Student

test_list_of_student = {
    Student("DFGHJK", "G.G.", 1, {'p.e': 4, 'math': 5, 'literature': 6, 'geography': 7, 'biology': 8}),
    Student("FGHJKL", "D.F.", 1, {'p.e': 7, 'math': 7, 'literature': 7, 'geography': 7, 'biology': 7}),
    Student("DFGHJKL", "E.R.", 2, {'p.e': 1, 'math': 8, 'literature': 8, 'geography': 8, 'biology': 8}),
    Student("DFGHJK", "W.D.", 2, {'p.e': 9, 'math': 9, 'literature': 9, 'geography': 9, 'biology': 9}),
    Student("CFVGHJKL", "F.A.", 3, {'p.e': 1, 'math': 1, 'literature': 10, 'geography': 10, 'biology': 10}),
    Student("FGHJK", "Q.C.", 3, {'p.e': 6, 'math': 6, 'literature': 6, 'geography': 6, 'biology': 6})
}


class TestStudentClass(unittest.TestCase):

    def setUp(self):
        self.student = Student("DFGHJK", "G.G.", 1,
                               {'p.e': 4, 'math': 5, 'literature': 6, 'geography': 7, 'biology': 8})

    def test_student_name(self):
        self.assertEqual(self.student.first_name, 'DFGHJK')

    def test_student_initials(self):
        self.assertEqual(self.student.initials, 'G.G.')

    def test_student_group_num(self):
        assert self.student.group_num == 1

    def test_student_marks(self):
        self.assertEqual(self.student.marks, {'p.e': 4, 'math': 5, 'literature': 6, 'geography': 7, 'biology': 8})


class TestSchoolClass(unittest.TestCase):
    def setUp(self):
        self.school = School()
        for num in range(1, 4):
            self.school.group(num)

        for student in test_list_of_student:
            self.school.add_student(student)

    def test_group_num_count(self):

        groups = (len(self.school.school_class.keys()))
        self.assertEqual(groups, 3), 'groups count should be equal to 3'

    def test_group_names(self):
        expected_result = ['1', '2', '3']
        test_result = []
        for key in self.school.school_class.keys():
            test_result.append(key)
        self.assertEqual(test_result, expected_result)



class TestSchoolMethods(unittest.TestCase):

    def setUp(self):
        self.school = School()
        for num in range(1, 4):
            self.school.group(num)

        for student in test_list_of_student:
            self.school.add_student(student)

    def test_average_5_6(self):

        expected_list = ['DFGHJK', 'FGHJK']
        test_list = []
        for value in self.school.school_class.values():
            for student in value:
                average = sum(student.marks.values()) / 5

                if 5 <= average <= 6:
                    test_list.append(student.first_name)

        self.assertEqual(expected_list, test_list)

    def test_more_than_7(self):

        expected_list = ["D.F", "W.D."]
        test_list = []

        for value in self.school.school_class.values():
            for student in value:
                average = sum(student.marks.values()) / 5

                if average >= 7:
                    test_list.append(student.initials)

        assert expected_list.sort() == test_list.sort()

    def test_get_by_group(self):
        expected_list = ["DFGHJKL", "DFGHJK"]
        test_list = []

        group_num = '2'
        students_group = self.school.school_class[group_num]

        for student in students_group:
            test_list.append(student.first_name)

        assert expected_list.sort() == test_list.sort()


if __name__ == '__main__':
    unittest.main()
