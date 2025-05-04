class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.students.append(self)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_hw(self):
        grade_list = []
        for val in self.grades.values():
            grade_list.extend(val)
        sum_ = sum(grade_list)  # Подсчет суммы оценок
        self.average_grade = round(sum_ / len(grade_list), 2)  # Подсчет среднего значения всех оценок
        return self.average_grade

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.average_grade_hw()}\n'
                  f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                  f'Завершенные курсы: {self.finished_courses}')
        return result

    def __lt__(self, other):
        if self.average_grade_hw() > other.average_grade_hw():
            return f'{self.name} {self.surname} средняя оценка больше'
        elif self.average_grade_hw() == other.average_grade_hw():
            return f'Cредние оценки равны'
        else:
            return f'{self.name} {self.surname} средняя оценка меньше'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lecturers.append(self)

    def average_grade_lec(self):
        grade_list = []
        for val in self.grades.values():
            grade_list.extend(val)
        sum_grades = sum(grade_list)
        self.average_grade = round(sum_grades / len(grade_list), 2)
        return self.average_grade

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self.average_grade_lec()}')
        return result

    def __lt__(self, other):
        if self.average_grade_lec() > other.average_grade_lec():
            return f'{self.name} {self.surname} средняя оценка больше'
        elif self.average_grade_lec() == other.average_grade_lec():
            return f'Cредние оценки равны'
        else:
            return f'{self.name} {self.surname} средняя оценка меньше'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


def average_grade_students_course(students, course):
    all_grades_course = []
    for student in students:
        for key, vul in student.grades.items():
            if key == course:
                all_grades_course.extend(vul)
    sum_grades = sum(all_grades_course)
    average_grade_student = round(sum_grades / len(all_grades_course), 1)
    return average_grade_student

def average_grade_lecturer_course (lecturers,course):
    all_grades_lecturer_course = []
    for lecturer in lecturers:
        if len(lecturer.grades) > 0:
            for key, vul in lecturer.grades.items():
                if key == course:
                    all_grades_lecturer_course.extend(vul)
    sum_grades = sum(all_grades_lecturer_course)
    average_grade_lecturer = round(sum_grades / len(all_grades_lecturer_course), 1)
    return average_grade_lecturer


student1 = Student('Гриша', 'Минин', 'м')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student2 = Student('Света', 'Осипова', 'ж')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['1с программирование']


lecturer1 = Lecturer('Ольга', 'Зимина')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['1с программирование']

lecturer2 = Lecturer('Игорь', 'Самойлов')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Sveta', 'Os')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']
print(reviewer1.courses_attached)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 6)

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, '1с программирование', 6)

student1.rate_lec(lecturer1,'Python', 6)
student1.rate_lec(lecturer1,'Git', 10)
student2.rate_lec(lecturer2,'Python', 2)
student2.rate_lec(lecturer2,'Python', 2)
student1.rate_lec(lecturer2,'Python', 2)
student2.rate_lec(lecturer1,'Python', 8)
print(lecturer1.grades)
print(lecturer2.grades)
print(student1.grades)
print(student2.grades)
print(reviewer1)
print(lecturer2)
print(student2)
print(student1 > student2)
print(lecturer1 > lecturer2)


print(average_grade_students_course(Student.students, 'Python'))
print(average_grade_students_course(Student.students, 'Python'))
print(average_grade_students_course(Student.students, 'Git'))


print(average_grade_lecturer_course(Lecturer.lecturers,'Python'))