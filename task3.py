class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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

best_student = Student('Ruoy', 'Eman', 'м')
best_student.courses_in_progress += ['Python']
best_student2 = Student('Ruoy2', 'Eman2', 'ж')
best_student2.courses_in_progress += ['Python']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
no_cool_mentor = Lecturer('Some2', 'Buddy2')
no_cool_mentor.courses_attached += ['Python']

cool_mentor2 = Reviewer('Sveta', 'Os')
cool_mentor2.courses_attached += ['Python']
print(cool_mentor2.courses_attached)

cool_mentor2.rate_hw(best_student, 'Python', 10)
cool_mentor2.rate_hw(best_student, 'Python', 6)
cool_mentor2.rate_hw(best_student, 'Python', 6)
cool_mentor2.rate_hw(best_student2, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Python', 6)

best_student.rate_lec(cool_mentor,'Python', 6)
best_student.rate_lec(cool_mentor,'Python', 10)
best_student2.rate_lec(no_cool_mentor,'Python', 2)
best_student.rate_lec(no_cool_mentor,'Python', 2)
best_student.rate_lec(no_cool_mentor,'Python', 2)
best_student2.rate_lec(cool_mentor,'Python', 8)
print(cool_mentor.grades)
print(best_student.grades)
print(cool_mentor2)
print(cool_mentor)
print(best_student)
print(best_student > best_student2)
print(cool_mentor > no_cool_mentor)