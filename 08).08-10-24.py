#super()

class person:
    def __init__(self,name, age):
        self.name = name
        self.age  = age
 
    def m1(self):
        print(self.name)
        print(self.age)
class employee(person):
    def __init__(self,name,age, id, salary ):
        super().__init__(name, age)
        self.id = id
        self.salary  = salary
 
    def m1(self):
        super().m1()
        print(self.id)
        print(self.salary)
 
e1 = employee("jaya",30,1005, 90000)
e1.m1()
 
class P:
    def __init__(self):
        print("this is parent class contsructor")
 
    def m1(self):
        print("this is parent class  instance")
 
    @classmethod
    def m2(self):
        print("this is parent class  classmethod")
 
    @staticmethod
    def m3():
        print("this is parent class  staticmethod")
 
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def display(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
   
    @staticmethod
    def m4():
        #super().m1()
        super(C,C).m3()       #only way to access parent class static method from child class static method
        #super().m2()
        #super().m3()
 
    @classmethod
    def m5(cls):
        super(C,cls).__init__(cls)   #access parent class constructor
        super(C,cls).m1(cls)         #acces parent class instnace
        #super().m1()
 
c = C()
c.display()
print("------------------")
c.m4()
 
print("---------------")
c.m5()

#method overriding
class Vehicle():
    def move(self):
        print("Vehicle is used for travelling")
class Bike(Vehicle):
    def move(self):
        print("Bike is used for move one place to onother place")
bike = Bike()
bike.move()

class P:
    def skills(self):
        print("fullstack, communication,fresher")
    def hire(self):
        print("we can hire him ")
class C(P):
    def hire(self):
        print("we will get back to you")
        print("we can hire experince person ")
 
c = C()
c.skills()
c.hire()


#operator overloading

class Grade():
    def __init__(self,grade):
        self.grade = grade
    def __add__(self,other):
        return self.grade + other.grade
grade1 = Grade(99)
grade2 = Grade(92)
print(grade1+grade2)
# print(Grade.__add__(grade1,grade2))