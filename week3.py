#Create Functions for Common Calculations

'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
'''

#Build a Currency Converter using Functions

''' def inr_to_usd(inr):
    return inr / 83.10       # example rate

def inr_to_eur(inr):
    return inr / 89.33

def inr_to_gbp(inr):
    return inr / 102.56

amount = 1000
print(inr_to_usd(amount))
print(inr_to_eur(amount))
'''

#Create a Student Database using Dictionaries
'''
students = {
    101: {"name": "Rahul", "age": 21, "course": "MCA"},
    102: {"name": "Aisha", "age": 22, "course": "BCA"},
}

# Print specific student
print(students[101]["name"])

# Add new student
students[103] = {"name": "Karan", "age": 23, "course": "MBA"}

# Display all students
for roll, info in students.items():
    print(roll, info)
    '''


#Text Analyzer (Counts Words & Characters)

'''
def text_analyzer(text):
    words = text.split()
    num_words = len(words)
    num_characters = len(text)
    return num_words, num_characters

sentence = "Python is amazing"
words, characters = text_analyzer(sentence)

print("Words:", words)
print("Characters:", characters)

'''

#Simple Bank Account System

'''
balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

def check_balance():
    print("Current Balance:", balance)

deposit(2000)
withdraw(500)
check_balance()
'''

#Practice with String Methods

'''
text = "hello python programming"

print(text.upper())
print(text.lower())
print(text.split())
print(text.replace("python", "world"))
print(text.title())
'''
