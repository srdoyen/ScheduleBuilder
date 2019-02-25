'''
Documentation, License etc.

@package ScheduleBuilder
'''
#import person, student, course
import Course
import Student
courses = []
students = []


def addCourses(schedule):
    global courses
    with open(schedule) as f:
        content = f.read().splitlines()
    for i in range(0,len(content)):
        c = content[i].split(',')
        courses.append(Course.Course(int(c[0]),c[1],int(c[2]),c[3]))
    return courses
    

def addStudents(studentList):
    global students
    with open(studentList) as f:
        content = f.read().splitlines()
    for i in range(0,len(content)):
        c = content[i].split(',')
        print(c)
        print(c[0], c[1])
        s = Student.Student(name=c[1], ID=int(c[0]))
        numCourses = int(c[2])
        for n in range(0,numCourses):
            addbyName(s,c[3+2*n])
            s.addCourse(c[3+2*n],int(c[4+2*n]))
        students.append(s)

            
    
    return students

def addbyID(student, courseID=0):
    global courses

    for i in range(0,len(courses)):
        if(courses[i].getID() == courseID):
            if(student in courses[i].students):
                print("Student is already in course:", courses[i].getName())
                return False
            else:
                courses[i].addStudent(student)
                return courses[i].getName()

    return False

def addbyName(student, courseName=""):
    global courses

    for i in range(0,len(courses)):
        if(courses[i].getName() == courseName):
            if(student in courses[i].students):
                print("Student is already in course.", courses[i].getName())
                return False
            else:
                courses[i].addStudent(student)
            return courseName        
    return False

def searchClass(student, course=""):
    global courses
    if(course.isdigit()):
        for i in range(0,len(courses)):
            if(courses[i].getID() == int(course)):
                print(courses[i].getID(), ": ", courses[i].getName())
    else:
        for i in range(0,len(courses)):
            if(courses[i].getName() == course):
                print(courses[i].getID(), ": ", courses[i].getName())
    return False

def showClasses(student):
    global courses
    for i in range(0,len(courses)):
        print(courses[i].getID(), ": ", courses[i].getName(), "(", courses[i].capacity - len(courses[i].students), "seats left )")
    return False

def prompt():
    global courses, students
    result=True
    print("Welcome to Schedule Builder!")
    print("1) Student")
    print("2) Teacher")
    x = int(input("What is your position? "))
    print("\n")
    sName = ""
    if(x==1):
        sID = input("Enter your Student ID: ")
        for j in range(0, len(students)):
            if((students[j]).getID() == int(sID)):
                s = students[j]
                sName = s.getName()
        
        if(sName == ""):
            print("No student with that ID was found. Follow instructions below\n")
            sName = input("Enter your Name: ")
            s = Student.Student(name=sName, ID=len(students))       
            print("Your ID number is: ", len(students))
            students.append(s)
            
        while(result):
            result = studentPrompt(s)
            
    elif(x==2):
        tID = print("Enter your Teacher ID: ")
        result = teacherPrompt(tID)
    else:
        result = True
        print("Wrong selection\n")
 
    print("\n")
    return result

def studentPrompt(s):
    global courses
    #new
    #s = student
    print("1) Add Class by ID")
    print("2) Add Class by Name")
    print("3) Search for Class")
    print("4) Show available Classes")
    print("5) Show my grades")
    print("6) QUIT")
    x = int(input("Enter selection: "))
    print("\n")
   
    if(x==1): #add Class by ID
        y = input("Enter Class ID: ")
        result = addbyID(s,int(y))
        if(result):
            s.addCourse(result)
    elif(x==2): #add Class by name
        y = input("Enter Class Name: ")
        result = addbyName(s,y)
        if(result):
            s.addCourse(result)
    elif(x==3): #search class by name
        z = input("Enter Class Name or ID: ")
        result = searchClass(s,z)
    elif(x==4): #search class by name
        print("Classes:\n")
        result = showClasses(s)
    elif(x==5):
        print("Grades:\n")
        result = s.printGrades()
    elif(x==6):
        print("QUITTING\n")
        return False
    else:
        print("Wrong Selection. Try again\n")
 
    print("\n")
    return True
    
def teacherPrompt(t):
    global courses
    print("IP\n")

def Main():
    courses = addCourses(schedule="winter.txt")
    students = addStudents(studentList="students.txt")
#
    prompt()
    #
    #teacher
    #teacherPrompt()

    for i in range(len(courses)):
        if(courses[i].students):
            print("Course: ", courses[i].getName())
            for j in range(0, len(courses[i].students)): 
                print((courses[i]).students[j].name)
                
    print(len(students))
    
            

if __name__ == '__main__':
    Main()
