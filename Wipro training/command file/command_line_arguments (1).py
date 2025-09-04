'''Write a program to accept two numbers as command line arguments and display their sum.'''
# import sys
# if len(sys.argv) != 3:
#     print("Usage: python command_line_arguments.py <num1> <num2>")
#     sys.exit(1)
# try:
#     num1 = int(sys.argv[1])
#     num2 = int(sys.argv[2])
#     total = num1 + num2
#     print("Sum:", total)
# except ValueError:
#     print("Please enter valid integers.")

'''Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.'''
# import sys
# if len(sys.argv) < 2:
#     print("Usage: python command_line_arguments.py <welcome_message>")
#     sys.exit(1)
# file_name = sys.argv[0]
# welcome_message = ' '.join(sys.argv[1:])
# print("File Name:", file_name)
# print("Welcome Message:", welcome_message)

'''Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.'''
# import sys
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
# if len(sys.argv) != 11:
#     print("Usage: python command_line_arguments.py <10 integers>")
#     sys.exit(1)
# try:
#     numbers = list(map(int, sys.argv[1:]))
#     prime_sum = sum(num for num in numbers if is_prime(num))
#     print("Sum of prime numbers:", prime_sum)
# except ValueError:
#     print("Please enter only valid integers.")