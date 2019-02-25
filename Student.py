
import Course
import ScheduleBuilder as up

class Student():
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.courses = []
        #self.grades = []   
      
    def addCourse(self, name="",grade=0):
        add = True
        for i in range(len(self.courses)):
            if(name == self.courses[i][0] and name):
                print(name, self.courses[i][0])
                add = False
        
        if(add):
            self.courses.append([name,grade])
    
    def removeCourse(self, courseID):
        print("removing course")
    
    def printGrades(self):
        for i in range(0, len(self.courses)):
            print(self.courses[i][0], self.courses[i][1])
        
    def getCourses(self):
        for i in range(len(self.courses)):
            print(self.courses[i][0])

    def getID(self):
        return self.ID

    def getName(self):
        return self.name
