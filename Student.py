class Student():
    enrolledCourses = {

    }
    def __init__(self, studentId, name, phoneNo):
        self.studentId = studentId
        self.name = name
        self.phoneNo = phoneNo
    
    def enrollCourse(self, Course):
        if Course not in self.enrolledCourses.keys():
            self.enrolledCourses.update({Course: 0})
    
    def updateScore(self, Course, score):
        if Course not in self.enrolledCourses.keys():
            self.enrolledCourses.update({Course: score})
        else:
            self.enrolledCourses[Course] = score
    
    def unenrollCourse(self, Course):
        if Course in self.enrolledCourses.keys():
            self.enrolledCourses.pop(Course)
    
    def calculateGPA(self):
        gpa = 0
        total_credits = 0
        for Course in self.enrolledCourses.keys():
            score = Course[score]
            credits = Course.credits
            gpa += score*credits
            total_credits += credits
        return gpa/(total_credits*10)
    
    def printStudentInfo(self):
        print("StudentID: ", self.studentId)
        print("Name: ", self.name)
        print("Phone Number: ", self.phoneNo)
        print("Enrolled Courses: ")
        for Course, score in self.enrolledCourses.items():
            print("Course: " + Course.courseName + " Score: " + str(score))
        



