#1. Student Class with Attributes & Methods

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

#2. BankAccount Class with Deposit & Withdraw

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

#3. Book Class for Library Management

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


#4. Car Class with Properties & Behaviors

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

 #5. Multiple Objects from Same Class
'''

s1 = Student("Rahul", 103, 95)
s2 = Student("Neha", 104, 89)
s3 = Student("Amit", 105, 91)

s1.display()
s2.display()
s3.display()

#6. Simple Inheritance Example


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



#Build a Library Management System using OOP with Book, Member, and Library classes with basic functionality                                    

'''
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Copies: {self.copies}")

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"Book borrowed successfully! Copies left: {self.copies}")
        else:
            print(" Book not available!")

    def return_book(self):
        self.copies += 1
        print(f"Book returned! Copies now: {self.copies}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            book.borrow()
            self.borrowed_books.append(book.title)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(" Book not available!")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(" You never borrowed this book!")

    def display(self):
        print(f"Member ID: {self.member_id} | Name: {self.name} | Borrowed: {self.borrowed_books}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully!")

    def show_books(self):
        print("\n Available Books:")
        for book in self.books:
            book.display()
        print()

    def show_members(self):
        print("\n👤 Registered Members:")
        for member in self.members:
            member.display()
        print()


# ---------------------- Driver Code ----------------------
library = Library()

# Add books
b1 = Book(1, "Python Programming", "ABC", 3)
b2 = Book(2, "Data Structures", "XYZ", 2)
library.add_book(b1)
library.add_book(b2)

# Register members
m1 = Member(101, "Ashu")
m2 = Member(102, "Ravi")
library.register_member(m1)
library.register_member(m2)

# Perform actions
library.show_books()
m1.borrow_book(b1)
m2.borrow_book(b1)
m1.return_book(b1)
library.show_books()
library.show_members()


'''