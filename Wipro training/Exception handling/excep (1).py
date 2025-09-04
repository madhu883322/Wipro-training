#1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except Exception as e:
    print("Error:", e)

#2. Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than a number, handle the exception and print an error message.
try:
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
    else:
        print("Not a prime number")
except Exception as e:
    print("Error:", e)

#3.Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
file_name = input("Enter file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content.title())
except Exception as e:
    print("Error:", e)

#4.Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
numbers = [5, -3, 7, -1, 0, 12, -8, 4, -6, 9]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print("Positive number")
    elif value < 0:
        print("Negative number")
    else:
        print("Zero")
except Exception as e:
    print("Error:", e)
