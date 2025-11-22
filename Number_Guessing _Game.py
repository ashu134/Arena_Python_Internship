
''' import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret:
        print("🎉 Correct! You guessed the right number!")
        break
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
        '''



# Age Category Program
'''
age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif age < 20:
    print("Category: Teen")
else:
    print("Category: Adult")
    '''


#Shopping List Manager
'''
shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found!")
    elif choice == 3:
        print("Shopping List:", shopping_list)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
        '''


#Multiplication Table Generator

"""
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    """

#Simple Login System

'''
username = "admin"
password = "12345"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login successful ")
else:
    print("Login failed ")
    '''

#Practice with List Operations
'''
numbers = [10, 20, 30, 40, 50]

print("Original:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(40)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length:", len(numbers))
'''
