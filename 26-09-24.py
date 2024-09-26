# 1.Create a class Person that has instance variables name, age, and gender. Add methods to:
# Initialize these variables.
# Update the age.
# Display the person's information.
#  Exercise:
#  > Create multiple instances of the Person class.
#  > Change the age of one person and display the updated information.
class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def info(self):
        print("***Person information***")
        print("name:",self.name)
        print("age:",self.age)
        print("gendar:",self.gender)
    def update_age(self,new_age):
        self.age = new_age
print("--------------Before updating age-------------")
p1 = person("raju",24,"male")
p1.info()
p2 = person("ravi",32,"male")
p2.info()
p3 = person("sita",25,"female")
p3.info()
print("--------------After updating age-------------")
p2.update_age(80)
p2.info()


# 2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
#   Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
#   Exercise:
#    >Create multiple employee instances.
#    >Print the total number of employees after adding each new employee.
#    >Check whether changing the total_employees in one instance affects the others.
class Company:
    total=0
    def __init__(self):
        self.employees={}
    def employee_info(self,name,department):
        self.employees[name]=department
        Company.total+=1 #accessing static variable inside insatance method using class name
        print("employee name: ",name, "Dept: ",department )
em=Company()
em.employee_info("Raju","Teste")  
em.employee_info("vibhav","Tester")
em.employee_info("Mahesh","Software Executive")
print("Total Employees: ",Company.total)  #Here Total employees is static variable we have to access outside class using class name
 
 
# 3.Create a class Rectangle that has instance variables length and width. 
#   Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
#   Exercise:
#     >Create instances of the Rectangle class with different lengths and widths.
#     >Calculate and print the area for each rectangle.
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length*self.width #storing data in local variable
        print(f"rectangle of having length {self.length} and width {self.width} then area is :{area}")
r1 = rectangle(20,30)
r1.calculate_area()  
r2 = rectangle(10,30)
r2.calculate_area()


# 4.Create a class Employee where:
#   Each employee has an instance variable salary.
#   There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
#   Write a method total_salary that calculates the total salary for an employee (including the bonus).
#   Exercise:
#    >Create several employee instances with different salaries.
#    >Change the bonus amount (static variable) and see how it affects all employees.
#    >Calculate and print the total salary for each employe
class employee:
    bonus = 0
    def __init__(self,salary):
        self.salary = salary
    def total_salary(self):
        return self.salary+employee.bonus
e1 = employee(300000)
e2 = employee(400000)
e3 = employee(500000)
employee.bonus = 100000
print("---------------Before changing bonus amount of an employees--------------")
print(f"total salary on employee1 :{e1.total_salary()}")
print(f"total salary on employee1 :{e2.total_salary()}")
print(f"total salary on employee1 :{e3.total_salary()}")
employee.bonus = 10000
print("---------------After changing bonus amount of an employees--------------")
print(f"total salary on employee1 :{e1.total_salary()}")
print(f"total salary on employee1 :{e2.total_salary()}")
print(f"total salary on employee1 :{e3.total_salary()}")