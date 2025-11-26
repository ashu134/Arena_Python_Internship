#Create a Program That Saves User Data to a File
 
'''
def save_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    with open("userdata.txt", "a") as f:
        f.write(f"{name}, {age}, {city}\n")

    print("Data saved successfully!")

save_user_data()
'''

#Build a Simple Diary Application

'''
def diary():
    entry = input("Write today's diary entry:\n")

    with open("diary.txt", "a") as f:
        f.write(entry + "\n---\n")

    print("Diary saved!")

diary()

'''

#Make a Program That Reads Data from CSV File

'''
import csv

def read_csv():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv()
'''

#Create a Quiz Game That Saves Scores

'''
def quiz():
    score = 0

    q1 = input("Capital of India? ")
    if q1.lower() == "delhi":
        score += 1

    q2 = input("2 + 3 = ? ")
    if q2 == "5":
        score += 1

    with open("scores.txt", "a") as f:
        f.write(f"Score: {score}\n")

    print("Your score saved!")

quiz()
'''

#Build a To-Do List That Persists Between Runs

'''
def add_task(task):
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    print("Task added!")

def view_tasks():
    try:
        with open("todo.txt", "r") as f:
            print("Your Tasks:")
            print(f.read())
    except FileNotFoundError:
        print("No tasks yet!")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        view_tasks()
    else:
        break
    '''

#Practice Handling File-Related Errors

'''
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist!")

    '''


#Personal Finance Tracker


'''
import csv
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Ensure file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
            print("File created successfully.\n")

# Add new expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, Bills, Shopping, Other): ")
        description = input("Enter description: ")

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        print("Expense added successfully!\n")

    except ValueError:
        print(" Invalid input! Amount must be a number.\n")

# Display all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print()
    except Exception as e:
        print("Error reading file:", e)

# Generate monthly report
def monthly_report():
    month = input("Enter month (MM example: 11): ")
    year = input("Enter year (YYYY example: 2025): ")

    total = 0
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Date"][5:7] == month and row["Date"][0:4] == year:
                    total += float(row["Amount"])
                    expenses.append(row)

        print(f"\n Monthly Report for {month}/{year}")
        for item in expenses:
            print(item)
        print(f"Total Spent: ₹{total}\n")

    except Exception as e:
        print("Error generating report:", e)

# Main menu
def main():
    initialize_file()

    while True:
        print("------ Personal Finance Tracker ------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_report()
        elif choice == '4':
            print("Thank you for using the tracker. Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
'''