#!/usr/bin/env python3
# Author ID: jacherubini

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            gpa = 0.0
        else:
            gpa = sum(self.courses.values()) / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    def displayCourses(self):
        passed_courses = []
        for course in self.courses:
            if self.courses[course] > 0.0:
                passed_courses.append(course)
        return passed_courses


if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')  # leading zeros retained
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
