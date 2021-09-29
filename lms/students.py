import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]


class Student:

    def __init__(self, first_name, last_name, email, age, address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender

    def add_student(self):
        student = {}
        for field in student_fields:
            student[field] = input('Enter {}\t'.format(field))
            if field == 'age':
                try:
                    int(student['age'])
                except:
                    student['age'] = input('Enter age as number\t')
        STUDENTS.append(student)

    def print_student(self, student):
        for field in student:
            print(field.title().replace("_", " "), ":", '\t', '\t', student[field])


class Group:

    def __init__(self):
        pass

    def load_students(self):
        for test_student in TEST_STUDENTS:
            STUDENTS.append(dict(zip(student_fields, test_student)))

    def dump_studens(self):
        with open('data/student_data.json', 'w') as file:
            json.dump(STUDENTS, file)

    def dump_csv(self):
        with open('data/student_data.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=student_fields)
            writer.writeheader()
            for student in STUDENTS:
                writer.writerow(student)

    def load_csv(self, file_path='data/student_data.csv'):
        with open(file_path, newline='') as file:
            reader = csv.reader(file)  # load_csv
            batch_data = list(reader)
            student = []
            for keys in batch_data:
                STUDENTS = {student_fields[i]: keys[i] for i in range(len(student_fields))}
                student.append(STUDENTS)
            dict_student = {'student_fields': student}
        print(dict_student)

    def load_from_json(self, file_path='data/student_data.json'):
        with open(file_path, 'r') as read_file:
            STUDENTS.extend(json.load(read_file))

    def calculate_avg_age(self):
        try:
            total_age = 0
            for student in STUDENTS:
                total_age += int(student['age'])
            avgerage_age = total_age / len(STUDENTS)
            print('Average age is {}'.format(avgerage_age))
        except ValueError:
            print('Cannot calculate average age')
        except Exception as e:
            print(str(e))

    def print_strudents_list(self):
        for student in STUDENTS:
            print(Student.print_student(student), "------------------------")


group = Group()
student = Student('Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F')

ACTIONS = {
    'add': student.add_student,
    'avg_age': group.calculate_avg_age,
    'load': group.load_students,
    'print': group.print_strudents_list,
    'dump': group.dump_studens,
    'dump_csv': group.dump_csv,
    'load_json': group.load_from_json,
    'load_csv': group.load_csv
}

if __name__ == '__main__':
    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            ACTIONS.get(action)()
        else:
            break






