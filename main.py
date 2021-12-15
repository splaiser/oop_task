class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        username = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average()}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return username

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        value = []
        count = 0
        for values in self.grades.values():
            value += values
            count += len(values)
        average_grades = sum(value) / count
        return average_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = {}

    def __str__(self):
        lecturer_name = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}\n'
        return lecturer_name

    def average(self):
        value = []
        count = 0
        for values in self.grades.values():
            value += values
            count += len(values)
        average_grades = sum(value) / count
        return average_grades


class Reviewer(Mentor):
    def __str__(self):
        reviewer_name = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return reviewer_name

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
worst_student = Student('Jhon', 'Jhonson', 'your_gender')
best_student.courses_in_progress += ['Python', 'C']
best_student.finished_courses += ['PHP']
worst_student.courses_in_progress += ['C#', 'PHP']
worst_student.finished_courses += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_lecturer = Lecturer('Lec1', 'Friend')
best_lecturer = Lecturer('Lec2', 'Proff')
cool_reviewer.courses_attached += ['Python', 'C', 'C#', 'PHP']

cool_lecturer.courses_attached += ['Python', 'C', 'PHP']
best_lecturer.courses_attached += ['Python', 'C#']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C', 2)
cool_reviewer.rate_hw(best_student, 'C', 5)
cool_reviewer.rate_hw(best_student, 'C', 8)
cool_reviewer.rate_hw(worst_student, 'C#', 5)
cool_reviewer.rate_hw(worst_student, 'C#', 10)
cool_reviewer.rate_hw(worst_student, 'C#', 8)
cool_reviewer.rate_hw(worst_student, 'PHP', 9)
cool_reviewer.rate_hw(worst_student, 'PHP', 9)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'C', 9)
best_student.rate_lecturer(cool_lecturer, 'C', 1)
best_student.rate_lecturer(best_lecturer, 'Python', 5)
best_student.rate_lecturer(best_lecturer, 'Python', 7)
best_student.rate_lecturer(best_lecturer, 'Python', 7)
worst_student.rate_lecturer(best_lecturer, 'C#', 5)
worst_student.rate_lecturer(best_lecturer, 'C#', 10)
worst_student.rate_lecturer(best_lecturer, 'C#', 10)
worst_student.rate_lecturer(cool_lecturer, 'PHP', 8)
worst_student.rate_lecturer(cool_lecturer, 'PHP', 9)

print(cool_reviewer)

print(cool_lecturer)

print(best_lecturer)

print(best_student)

print(worst_student)
