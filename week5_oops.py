#Student Class with Attributes & Methods

'''
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")

# Creating objects
s1 = Student("Ashu", 101, 88)
s2 = Student("Ravi", 102, 92)

s1.display()
s2.display()
'''

#BankAccount Class with Deposit & Withdraw


'''
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount} | New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount} | Remaining Balance: ₹{self.balance}")

# Use class
account1 = BankAccount("Ashu", 1000)
account1.deposit(500)
account1.withdraw(300)

'''

#Book Class for Library Management


'''
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"{self.title} borrowed successfully. Copies left: {self.copies}")
        else:
            print("Book not available!")

    def return_book(self):
        self.copies += 1
        print(f"{self.title} returned. Copies now: {self.copies}")

book1 = Book("Python Basics", "ABC", 3)
book1.borrow_book()
book1.return_book()
'''

#Car Class with Properties & Behaviors


'''
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.brand} {self.model} has started.")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")

car1 = Car("BMW", "X5", "Black")
car1.start()
car1.stop()
'''

#Multiple Objects from Same Class


'''
s1 = Student("Rahul", 103, 95)
s2 = Student("Neha", 104, 89)
s3 = Student("Amit", 105, 91)

s1.display()
s2.display()
s3.display()


'''


#Simple Inheritance Example

'''
class Animal:
    def sound(self):
        print("Animal makes some sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

'''