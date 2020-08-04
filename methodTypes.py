class Student:

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student class")

s1 = Student(34,54,56)
s2 = Student(45,67,85)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
