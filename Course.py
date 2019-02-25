
class Course():
    def __init__(self, ID, name, capacity, teacher):
        self.ID = ID    
        self.name = name
        self.capacity = capacity
        self.teacher = teacher
        self.students = []
        self.avg = 0       
      
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name  
    
    def getPosition(self):
        return self.position
    
    def getStudents(self):
        return self.students
    
    def getTeacher(self):
        return self.teacher
    
    def getAvg(self):
        return self.avg
    
    def addStudent(self, student):
        if(len(self.students)== self.capacity):
            return False
        else:
            self.students.append(student)
            return True
    
