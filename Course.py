class Course():
    enrolledStudents = []
    def __init__(self, courseID, courseName, credits):
        self.courseID = courseID
        self.courseName = courseName
        self.credits = credits
    
    def addStudent(self, Student):
        if Student in self.enrolledStudents:
            pass
        else:
            self.enrolledStudents.append(Student)
    
    def removeStudent(self, Student):
        if Student in self.enrolledStudents:
            self.enrolledStudents.remove(Student)
    
    def calculateAverageGPA(self):
        averageGPA = 0
        for Student in self.enrolledStudents:
            averageGPA += Student.calculateGPA()
        return averageGPA
    
    def printCourseInfo(self):
        print("CourseID: ", self.courseID)
        print("Name: ", self.courseName)
        print("Credits: ", self.credits)
        
    