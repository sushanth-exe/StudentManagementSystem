from Student import Student
from Course import Course
totalStudents = {}
totalCourses = {}

def addStudent():
    studentID = ""
    studentName = ""
    studentPhoneNo = ""
    while(1):
        print("Enter Student ID: ", end = "")
        studentID = input()
        if len(studentID) > 0:
            break
    if studentID in totalStudents.keys():
        print("Student already exists")
        return
    while(1):
        print("Enter Student Name: ", end = "")
        studentName = input()
        if len(studentName) > 0:
            break
    while(1):
        print("Enter Student Phone No.: ", end = "")
        studentPhoneNo = input()
        if len(studentPhoneNo) > 0:
            break
    newStudent = Student(studentID, studentName, studentPhoneNo)
    totalStudents.update({studentID: newStudent})

def addCourse():
    courseID = ""
    courseName = ""
    courseCredits = ""
    while(1):
        print("Enter Course ID: ", end = "")
        courseID = input()
        if len(courseID) > 0:
            break
    if courseID in totalCourses.keys():
        print("Course already exists")
        return
    while(1):
        print("Enter Course Name: ", end = "")
        courseName = input()
        if len(courseName) > 0:
            break
    while(1):
        print("Enter Course Credits: ", end = "")
        try:
            courseCredits = int(input())
            break
        except:
            print("Enter a number")
    newCourse = Course(courseID, courseName, courseCredits)
    totalCourses.update({courseID: newCourse})

def addStudentToCourse():
    courseID = ""
    studentID = ""
    while(1):
        print("Enter Course ID: ", end = "")
        courseID = input()
        if len(courseID) > 0:
            break
    while(1):
        print("Enter Student ID: ", end = "")
        studentID = input()
        if len(studentID) > 0:
            break
    if courseID in totalCourses.keys() and studentID in totalStudents.keys():
        course = totalCourses[courseID]
        student = totalStudents[studentID]
        course.addStudent(student)
        student.enrollCourse(course)
    else:
        print("Course or Student doesn't exist")
    
def removeStudentFromCourse():
    courseID = ""
    studentID = ""
    while(1):
        print("Enter Course ID: ", end = "")
        courseID = input()
        if len(courseID) > 0:
            break
    while(1):
        print("Enter Student ID: ", end = "")
        studentID = input()
        if len(studentID) > 0:
            break
    if courseID in totalCourses.keys() and studentID in totalStudents.keys():
        course = totalCourses[courseID]
        student = totalStudents[studentID]
        course.removeStudent(student)
        student.unenrollCourse(course)
    else:
        print("Course or Student doesn't exist")

def updateScore():
    courseID = ""
    studentID = ""
    score = ""
    while(1):
        print("Enter Course ID: ", end = "")
        courseID = input()
        if len(courseID) > 0:
            break
    while(1):
        print("Enter Student ID: ", end = "")
        studentID = input()
        if len(studentID) > 0:
            break
    while(1):
        print("Enter Course Score: ", end = "")
        try:
            score = int(input())
            break
        except:
            print("Enter a number")
    if courseID in totalCourses.keys() and studentID in totalStudents.keys():
        course = totalCourses[courseID]
        student = totalStudents[studentID]
        student.updateScore(course, score)
    else:
        print("Course or Student doesn't exist")

def calculateGPA():
    studentID = ""
    while(1):
        print("Enter Student ID: ", end = "")
        studentID = input()
        if len(studentID) > 0:
            break
    if studentID not in totalStudents.keys():
        print("Student doesn't exist")
        return
    gpa = totalStudents[studentID].calculateGPA()
    print("GPA: ", gpa)

def calculateAverageGPA():
    courseID = ""
    while(1):
        print("Enter Student ID: ", end = "")
        courseID = input()
        if len(courseID) > 0:
            break
    if courseID not in totalCourses.keys():
        print("Course doesn't exist")
        return
    gpa = totalCourses[courseID].calculateAverageGPA()
    print("Average GPA: ", gpa)

def showInfo():
    for _, Student in totalStudents.items():
        Student.printStudentInfo()
        print("---")
    for _, Course in totalCourses.items():
        Course.printCourseInfo()
        print("---")

if __name__ == "__main__":
    print("Welcome to Student and Course Management System")
    while(1):
        print("Available Options: ")
        print("1. Add a Student")
        print("2. Add a Course")
        print("3. Add a student to a Course")
        print("4. Remove a student from a Course")
        print("5. Update Score for a Student in a Course")
        print("6. Calculate Student GPA")
        print("7. Calculate avg GPA")
        print("8. Show Complete Info")
        print("9. Exit")
        option = 0
        print("Enter a number from one of the options: ", end="")
        try:
            option = int(input())
            if option < 1 or option > 9:
                raise Exception
        except:
            print("Enter a number from 1 - 9 only")
        
        if option == 1:
            addStudent()
        elif option == 2:
            addCourse()
        elif option == 3:
            addStudentToCourse()
        elif option == 4:
            removeStudentFromCourse()
        elif option == 5:
            updateScore()
        elif option == 6:
            calculateGPA()
        elif option == 7:
            calculateAverageGPA()
        elif option == 8:
            showInfo()
        elif option == 9:
            exit()

        


