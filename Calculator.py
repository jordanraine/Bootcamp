from __future__ import division

#define functions

def add(x, y):
    #adds two numbers
    return x + y
#subtracts two numbers
def subtract (x, y):
    return x - y
#multiplies two numbers
def multiply (x, y):
    return x * y
#divides two numbers
def divide (x, y):
    return x / y


print("What would you like to do? ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
#ToDo make sure to solve if user doesnt input a number.
choice = raw_input("Enter your choice(1/4):")

num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: "))

if choice == '1':
    print(num1,'+',num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == "4":
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")

