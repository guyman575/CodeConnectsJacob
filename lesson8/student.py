from schoolutils import getGradePoint
class Student(): 
    # grades = {}
    # name = default

    def __init__(self,name="default",grades={}):
        self.name = name
        self.grades = grades

    def getName(self):
        return self.name

    def getGrade(self,class_name):
        return self.grades[class_name]

    def setGrade(self,class_name,grade):
        self.grades[class_name] = int(grade)

    def printGrade(self,class_name):
        if class_name in self.grades:
            print(f"{self.name} has a grade of {self.getGrade(class_name)} in {class_name}")
        else:
            print (f"{self.name} does not take {class_name}")
    
    def getGPA(self,grades):
        total = 0

        for key,value in self.grades.items():
            total += value
    
        return total / len(self.grades)            



