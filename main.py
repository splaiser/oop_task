class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades_dict = {}

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
        for course, values in self.grades.items():
            value += values
            count += len(values)
            self.average_grades_dict[course] = sum(values) / count
        average_grades = sum(value) / count
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нет такого студента!")
            return
        else:
            if self.average() < other.average():
                print(f'{other.name} учиться лучше чем {self.name}! Будь как {other.name}!')
            elif self.average() > other.average():
                print(f'{self.name} учиться лучше чем {other.name}! Будь как {self.name}!')
            return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_grades_dict = {}


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
        for course, values in self.grades.items():
            value += values
            count += len(values)
            self.average_grades_dict[course] = sum(values) / count
        average_grades = sum(value) / count
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нет такого Лектора!")
            return
        else:
            if self.average() < other.average():
                print(f'{other.name} преподает лучше чем {self.name}!')
            elif self.average() > other.average():
                print(f'{self.name} преподает лучше чем {other.name}!')
            return


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


best_student = Student('Ruby', 'Eman', 'your_gender')
worst_student = Student('Jhon', 'Johnson', 'your_gender')
best_student.courses_in_progress += ['Python', 'C', 'PHP']
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
cool_reviewer.rate_hw(best_student, 'PHP', 8)
cool_reviewer.rate_hw(best_student, 'PHP', 4)
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
best_student.rate_lecturer(cool_lecturer, 'PHP', 2)
best_student.rate_lecturer(cool_lecturer, 'PHP', 3)

print(cool_reviewer)

print(cool_lecturer)

print(best_lecturer)

print(best_student)

print(worst_student)

Student.__lt__(best_student, worst_student)
Student.__lt__(worst_student, best_student)
Lecturer.__lt__(best_lecturer, cool_lecturer)
Lecturer.__lt__(cool_lecturer, best_lecturer)

our_students = [best_student, worst_student]
our_lecturer = [best_lecturer, cool_lecturer]


def average_course_rate(student_list, course):
    final_list = []
    for student in student_list:
        for key, value in student.average_grades_dict.items():
            if key == course:
                final_list.append(value)
    return sum(final_list) / len(final_list)


def average_lecture_rate(lecturer_list, course):
    final_list = []
    for lecturer in lecturer_list:
        for key, value in lecturer.average_grades_dict.items():
            if key == course:
                final_list.append(value)
    return sum(final_list) / len(final_list)

print(average_course_rate(our_students, 'PHP'))
print(average_lecture_rate(our_lecturer, 'Python'))
