# Dictionary to store students and their grades
grade_book = {}

# Define the Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if self.grades:
            total = sum(self.grades.values())
            average = total / len(self.grades)
            return average
        else:
            return None

# Function to add a new student
def add_student():
    name = input("\nEnter the name of the student you'd like to add: ").strip().capitalize()
    if name in grade_book:
        print(f"{name} is already in the grade book!")
    else:
        grade_book[name] = Student(name)
        print(f"Successfully added {name} to the grade book.")

# Function to add a grade for a student
def add_grade():
    name = input("\nEnter the student's name: ").strip().capitalize()
    if name not in grade_book:
        print(f"{name} is not found in the grade book. Please add the student first.")
    else:
        subject = input("Enter the subject for the grade: ").strip().capitalize()
        try:
            grade = float(input(f"Enter {name}'s grade for {subject}: "))
            grade_book[name].add_grade(subject, grade)
            print(f"Added grade for {subject}: {grade} for {name}.")
        except ValueError:
            print("Invalid grade input. Please enter a numerical value.")

# Function to view the average grade for a student
def view_average():
    name = input("\nEnter the name of the student to view their average grade: ").strip().capitalize()
    if name in grade_book:
        average = grade_book[name].calculate_average()
        if average is not None:
            print(f"{name}'s average grade is: {average:.2f}")
        else:
            print(f"No grades available for {name}.")
    else:
        print(f"{name} is not in the grade book. Please add the student first.")

# Function to display all students in the grade book
def display_students():
    if grade_book:
        print("\nCurrent Students in the Grade Book:")
        for student in grade_book:
            print(f"- {student}")
    else:
        print("\nNo students in the grade book yet.")

# Main program loop with improved UI
def main():
    print("Welcome to the Student Grade Book!")

    while True:
        # Display the list of students at the beginning of each menu loop
        display_students()
        
        print("\nAvailable Actions:")
        print("1. Add a new student")
        print("2. Add or update a grade for an existing student")
        print("3. View a student's average grade")
        print("4. Exit the program")

        choice = input("\nChoose an action by entering the corresponding number: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_average()
        elif choice == "4":
            print("Goodbye! Exiting the Student Grade Book.")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 4.")

# Run the program
main()
