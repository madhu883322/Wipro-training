# 1. Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check if a number is Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Check if two numbers have the same last digit
def lastDigit(a, b):
    return a % 10 == b % 10

print(lastDigit(7, 17))   # True
print(lastDigit(6, 17))   # False
print(lastDigit(3, 113))  # True


# 4. Print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")
print()  # for newline


# 5. Print even numbers between 23 and 57 (each in a new line)
for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# 6. Check if a given number is prime
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# 7. Print prime numbers between 10 and 99
for num in range(10, 100):
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# 8. Sum of all digits of a given number
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num = num // 10
print("Sum of digits:", total)


# 9. Reverse a given number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num = num // 10
print("Reversed number:", reverse)
