'''Write a function to return the sum of all numbers in a list.'''
# def sum_of_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(sum_of_list([8, 2, 3, 6, 7]))

'''Write a function to return the reverse of a string.'''
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str
# print(reverse_string("1234abcd"))

'''Write a function to calculate and return the factorial of a number (a non-negative integer).'''
# def fact(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# print(fact(5))

'''Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.'''
# def count_case_letters(s):
#     upper_count = 0
#     lower_count = 0
#     for char in s:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     print("Uppercase letters:", upper_count)
#     print("Lowercase letters:", lower_count)
# count_case_letters("Hello World!")

'''Write a function to print the even numbers from a given list. List is passed to the function as an argument.'''
# def print_even_numbers(numbers):
#     even_numbers = [num for num in numbers if num % 2 == 0]
#     print("Even numbers:", even_numbers)
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_even_numbers(sample_list)

'''Write a function that takes a number as a parameter and checks whether the number is prime or not.'''
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# number = 29
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")