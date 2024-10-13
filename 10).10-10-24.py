# 1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and
#  year of the vehicle. Then, create two subclasses:
# Car, which adds an attribute number_of_doors.
# Motorcycle, which adds an attribute has_sidecar.
# Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return (f"brand: {self.brand} and year: {self.year}")

class Car(Vehicle):
    def __init__(self,brand,year,number_of_doors):
        super().__init__(brand,year)
        self.number_of_doors = number_of_doors
    
    def get_info(self):
        return (f"brand: {self.brand} , year: {self.year} and number of doors: {self.number_of_doors}")

class Motorcycle(Vehicle):
    def __init__(self,brand,year,has_sidecar):
        super().__init__(brand,year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return (f"brand: {self.brand} , year: {self.year} and side car: {self.has_sidecar}")

car = Car("KIA", 2021, 4)
print(car.get_info())
motorcycle = Motorcycle("Harley-Davidson", 2024, True)
print(motorcycle.get_info())


# 2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:
# Dog with the sound "Woof".
# Cat with the sound "Meow".
# Cow with the sound "Moo".
# Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)
play_sound(cat)
play_sound(cow)


# 3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:
# SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
# CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
# Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self._balance - amount >= 500:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds. Balance cannot go below $500.")
        else:
            print("Withdrawal amount must be positive.")

class CurrentAccount(BankAccount):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self._balance - amount >= -1000:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds. Overdraft limit is $1000.")
        else:
            print("Withdrawal amount must be positive.")

savings = SavingsAccount(1000)
current = CurrentAccount(1000)

savings.deposit(200)  
savings.withdraw(800) 
savings.withdraw(100) 

current.deposit(500) 
current.withdraw(2000) 
current.withdraw(600)  
        


# 4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:
# Manager, which adds an attribute department.
# Developer, which adds an attribute programming_language.
# Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.
# Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage. 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return "name: "+self.name + ", Salary: $" + str(self.salary)
    def get_salary(self):
        return self.salary
    def increase_salary(self,percent):
        self.salary+=self.salary*percent/100
class Manager(Employee):
     def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
     def get_details(self):
        return  super().get_details() + ", Department: " + self.department
class Developer(Employee):
    def __init__(self,name, salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def get_details(self):
        return super().get_details()+ ", programming language: " + self.programming_language
emp=Employee("Raju",20000)
mngr=Manager("Ravi",40000,"HR")
dev=Developer("Ritesh",80000,"python")
print(emp.get_details())
print(mngr.get_details())
print(dev.get_details())
emp.increase_salary(10)
mngr.increase_salary(10)
dev.increase_salary(10)
print("Details after increasing salary")
print(emp.get_details())
print(mngr.get_details())
print(dev.get_details())
 


# 5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:
# Audio, which plays a .mp3 file.
# Video, which plays a .mp4 file.
# LiveStream, which plays a live stream.
# Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate 
# polymorphism by passing different types of media to this function.
from abc import ABC,abstractmethod
class Media(ABC):
    @abstractmethod
    def play(self):
        pass
class Audio(Media):
    def __init__(self,file_name):
        self.mp3filename=file_name
    def play(self):
        print("playing audio file: ",self.mp3filename)
class Video(Media):
    def __init__(self,mp4file_name):
        self.mp4filename=mp4file_name
    def play(self):
        print("playing video file: ",self.mp4filename)
 
class LiveStream(Media):
    def __init__(self,livestream) -> None:
        self.livestream=livestream
    def play(self):
        print("Playing livestream: ",self.livestream)
def start_media(media):
    media.play()
audio=Audio("Background music")
video=Video("Cartoon film")
liveStream=LiveStream("Dandiya live show")
start_media(audio)
start_media(video)
start_media(liveStream)
 
# 6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:
# Book, with attributes title, author, and num_copies.
# DVD, with attributes title, director, and duration.
# Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or 
# marks the DVD as borrowed.
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            print(f"Borrowed '{self.title}'. Copies left: {self.num_copies}")
        else:
            print(f"No copies of '{self.title}' left to borrow.")

    def return_item(self):
        self.num_copies += 1
        print(f"Returned '{self.title}'. Copies available: {self.num_copies}")

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Borrowed DVD '{self.title}'.")
        else:
            print(f"DVD '{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Returned DVD '{self.title}'.")
        else:
            print(f"DVD '{self.title}' was not borrowed.")

def borrow_item(item):
    item.borrow()

book = Book("1984", "George Orwell", 3)
dvd = DVD("Inception", "Christopher Nolan", "148 minutes")

borrow_item(book) 
borrow_item(dvd)   

  

