#auto create file and write data to it
# file = open("student.txt", "w")
# file.write("Ahmad\n")
# file.write("Umar\n")
# file.write("Uzair\n")
# file.write("Shehzaib\n")
# file.write("Bilal\n")



# 2. read data from file
# file = open("student.txt", "r")
# print(file.read())



# 3. append data to file
# file = open("student.txt", "a")
# file.write("Umar bhai\n")
# file.write("#uzair\n")
# file.close()


#4. count the number of lines in the file
# file = open('student.txt', 'r') 
# lines = file.readlines()

# print(f"Total number of lines in 'student.txt': {len(lines)}")


# 5.  error hanlde if file not found
# try:
#     # with open("student.txt", "r") as file:

#     # if file not found 
#     with open("notfound.txt", "r") as file:

#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("Error: File not found.")
 

# 6. Read file and handle error
try:
    with open('student.txt', 'r') as file:
        print("File contents:\n", file.read())

    number = int(input("Enter marks: "))
    print("You entered:", number)

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Please enter a valid number.")



# 8. Divide two numbers (handle divide by zero)

try:
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# 9. Open a file (handle error)
filename = input("Enter filename: ")
try:
    f = open(filename, "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found!")


# 10. Class with attributes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basics", "Ahmad")
print("Title:", book1.title)
print("Author:", book1.author)


# 11. Add method in Book class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(f"The book title is {self.title} by Author {self.author}")

book2 = Book("OOP in Python", "Ali")
book2.show()


# 12. Student class with constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Ahmad", 21)
s1.display()


# 13. Calculator class

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error! Divide by zero"
        return a / b

c = Calculator()
print("Add:", c.add(5, 3))
print("Subtract:", c.subtract(5, 3))
print("Multiply:", c.multiply(5, 3))
print("Divide:", c.divide(5, 0))


# 14. Teacher inherits Person

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t1 = Teacher("Ali", "Math")
print("Name:", t1.name, "Subject:", t1.subject)


# 15. Method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# 16. Read file with error handling

try:
    with open("student.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found")
except PermissionError:
    print("Error: Permission denied")


# 17. Library class

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found!")

    def display_books(self):
        print("Books in library:", self.books)

lib = Library()
lib.add_book("Python")
lib.add_book("Math")
lib.display_books()
lib.remove_book("Science")


# 18. Store numbers in file and sum them

numbers = input("Enter numbers separated by space: ").split()
with open("nums.txt", "w") as f:
    for n in numbers:
        f.write(n + "\n")

total = 0
with open("nums.txt", "r") as f:
    for line in f:
        total += int(line)

print("Sum =", total)


# 19. Random numbers in file, find largest

import random
with open("random.txt", "w") as f:
    for i in range(10):
        num = random.randint(1, 100)
        f.write(str(num) + "\n")

with open("random.txt", "r") as f:
    numbers = [int(x) for x in f]

print("Largest =", max(numbers))


# 20. Employee class with bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_bonus(self, amount):
        self.salary += amount

e1 = Employee("Ahmad", 50000)
e1.give_bonus(5000)
print("Name:", e1.name, "Salary:", e1.salary)


# 21. Handle multiple exceptions

try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result =", a / b)
except (ZeroDivisionError, ValueError):
    print("Error: Invalid input or divide by zero")


# 22. Course class

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def display(self):
        print("Course:", self.course_name, "Duration:", self.duration)

c1 = Course("Python", "3 months")
c1.display()


# 23. Count words in text file

try:
    with open("text.txt", "r") as f:
        data = f.read()
        words = data.split()
        print("Word count =", len(words))
except FileNotFoundError:
    print("File not found")
