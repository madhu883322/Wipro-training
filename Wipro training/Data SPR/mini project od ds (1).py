# --------------------- Project 1 ---------------------
# Create a dictionary of people with interesting facts. Update and display.

import random

people = {
    "Jeff": "is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original facts
for person, fact in people.items():
    print(f"{person}: {fact}")
print()

# Change a fact
people["Jeff"] = "is afraid of heights."

# Add new person
people["Jill"] = "Can hula dance."

# Shuffle display order
items = list(people.items())
random.shuffle(items)
for person, fact in items:
    print(f"{person}: {fact}")

# --------------------- Project 2 ---------------------
# Find the runner-up score

scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
if len(unique_scores) >= 2:
    print("\nRunner-up score:", unique_scores[1])
else:
    print("\nNot enough unique scores for a runner-up.")

# --------------------- Project 3 ---------------------
# Average marks of a student from a dictionary

students = {
    "Krishna": [57, 68, 60],
    "Anjan": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("\nEnter a name: ")
if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage marks: {average:.2f}")
else:
    print("Student not found.")

# --------------------- Project 4 ---------------------
# Count how many times "Alex" appears in the string

text = "Hi Alex WelcomeAlex Bye Alex"
count = text.count("Alex")
print(f"\n'Alex' appears {count} times.")
