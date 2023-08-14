"""
Question-1: Creating a Basic Calculator

You are tasked with creating a simple calculator program that can perform addition, subtraction,
multiplication, and division operations. You need to create functions for each of these operations
and allow the user to input two numbers and choose an operation to perform.

Requirements:

1. Create four functions: add, subtract, multiply, and divide. Each function should take two arguments
(the two numbers to perform the operation on) and return the result of the operation.
2. Create a function named calculator that presents a menu to the user with options for each operation.
The user should be able to input their choice, as well as the two numbers for the operation.
3. After performing the selected operation, display the result to the user.
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def calculator():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
    if choice == "1":
        print(add(number1, number2))
    elif choice == "2":
        print(subtract(number1, number2))
    elif choice == "3":
        print(multiply(number1, number2))
    elif choice == "4":
        print(divide(number1, number2))
    else:
        print("Invalid input")

calculator()
