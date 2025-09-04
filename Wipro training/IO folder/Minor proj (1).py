from collections import Counter

with open('sample.txt', 'r') as file:
    lines = file.readlines()

meeting_time = len(lines)
if meeting_time > 12:
    meeting_time -= 12

words = []
for line in lines:
    for word in line.strip().split():
        word = word.strip('.,()"').lower()
        words.append(word)

most_common = Counter(words).most_common(1)[0][0].capitalize() + " Street"

print(f"Meeting time: {meeting_time} AM")
print(f"Meeting place: {most_common}")

