#Write a program to read the entire content from a txt file and display it to the user.
file_path = "example.txt"  
with open(file_path, 'r') as file:
    content = file.read()

print("File content:")
print(content)

#Write a program to read first n lines from a txt file. Get n as user input.
file_path = "example.txt"
n = int(input("Enter the number of lines to read: "))

with open(file_path, 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')

#Write a program to accept input from user and append it to a txt file.
file_path = "example.txt"
text = input("Enter text to append: ")
with open(file_path, 'a') as file:
    file.write(text + '\n')

#4. Write a program to read contents from a txt file line by line and store each line into a list.
file_path = "example.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip('\n') for line in lines]
print(lines)

#Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
file_path = "example.txt"
with open(file_path, 'r') as file:
    content = file.read()

words = content.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)

#Write a program to count the frequency of a user entered word in a txt file.
word_to_count = input("Enter the word to count: ")

with open(file_path, 'r') as file:
    content = file.read()

words = content.split()
count = words.count(word_to_count)
print("Frequency:", count)

#