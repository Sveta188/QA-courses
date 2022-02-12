import pytest
from class_work import Student, School

test_list_of_student = {
    Student("Ivanov", "I.G.", 1, {'p.e': 9, 'math': 9, 'literature': 9, 'geography': 9, 'biology': 9}),
    Student("Ivanov2", "O.S.", 2, {'p.e': 10, 'math': 10, 'literature': 10, 'geography': 10, 'biology': 10}),
    Student("Ivanov3", "A.E.", 3, {'p.e': 5, 'math': 6, 'literature': 6, 'geography': 6, 'biology': 6}),
    Student("Ivanov4", "A.E.", 3, {'p.e': 10, 'math': 10, 'literature': 10, 'geography': 6, 'biology': 6})}


@pytest.fixture
def create_student():
    student = Student("Ivanov", "I.G.", 1, {'p.e': 9, 'math': 9, 'literature': 9, 'geography': 9, 'biology': 9})
    return student


@pytest.fixture
def get_school():
    school = School()
    for num in range(1, 4):
        school.group(num)

    for student in test_list_of_student:
        school.add_student(student)
    return school


@pytest.mark.unit
class TestModulsClass:

    def test_student_name(self, create_student):
        assert create_student.first_name == 'Ivanov'

    def test_student_initials(self, create_student):
        assert create_student.initials == 'I.G.'

    def test_student_group_num(self, create_student):

        assert create_student.group_num == 1

    @pytest.mark.parametrize('student_lesson, exp_result', [
                             ('p.e', 9),
                             ('math', 9),
                             ('literature', 9),
                             ('geography', 9),
                             ('biology', 9)])
    def test_student_marks(self, create_student, student_lesson, exp_result):
        print('\n')
        print('')
        print(create_student.marks[student_lesson], exp_result)
        assert create_student.marks[student_lesson] == exp_result

    def test_group_num_count(self, get_school):
        groups_count = (len(get_school.school_class.keys()))
        assert groups_count == 3

    def test_group_names(self, get_school):
        expected_result = ['1', '2', '3']
        test_result = []
        for key in get_school.school_class.keys():
            test_result.append(key)
        assert test_result == expected_result

    @pytest.mark.xfail
    def test_group_names_fail(self, get_school):
        expected_result = ['4456789', '23456', '2134567']
        test_result = []
        for key in get_school.school_class.keys():
            test_result.append(key)
        assert test_result == expected_result


@pytest.mark.integration
class TestSchoolMethods:

    def test_by_5_6(self, get_school):

        expected_list = ['Ivanov3']
        test_list = []
        for value in get_school.school_class.values():
            for student in value:
                average = sum(student.marks.values()) / 5

                if 5 <= average <= 6:
                    test_list.append(student.first_name)

        assert expected_list == test_list

    def test_more_than_7(self, get_school):
        expected_list = ["I.G.", "O.S."]
        test_list = []

        for value in get_school.school_class.values():
            for student in value:
                average = sum(student.marks.values()) / 5

                if average >= 7:
                    test_list.append(student.initials)

        assert expected_list.sort() == test_list.sort(), '(test_list != "M.V.", "A.G.", "O.V.", "O.S.")'

    def test_get_mates(self, get_school):
        expected_list = ["Ivanov3", "Ivanov4"]
        test_list = []

        group_num = '3'
        students_group = get_school.school_class[group_num]

        for student in students_group:
            test_list.append(student.first_name)

        assert expected_list.sort() == test_list.sort()
