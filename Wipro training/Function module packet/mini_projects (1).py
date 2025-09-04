'''Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.'''
# def sort_colors_sequence(color_sequence: str) -> str:
#     colors = color_sequence.split("-")
#     colors.sort()
#     return "-".join(colors)
# if __name__ == "__main__":
#     print(sort_colors_sequence("green-red-yellow-black-white"))
#     print(sort_colors_sequence("PINK-BLUE-TAN-PURPLE"))

'''Create a Python module with the following functions:

ispalindrome(name):
Takes a name as input
Checks whether the name is a palindrome or not

count_the_vowels(name):
Takes a name as input
Counts how many vowels are present in the name

frequency_of_letters(name):
Takes a name as input
Counts how many times each letter appears in the name

Note:
The input name will be completely in either lowercase or uppercase
Import the module in another Python script
Test the functions by passing appropriate inputs'''
# import module

# def format_output(name):
#     if module.ispalindrome(name):
#         print("Yes it is a palindrome.")
#     else:
#         print("No it is not a palindrome.")
#     vowel_count = module.count_the_vowels(name)
#     print(f"No of vowels: {vowel_count}")
#     freq_dict = module.frequency_of_letters(name)
#     freq_output = ', '.join(f"{char}-{freq_dict[char]}" for char in sorted(freq_dict))
#     print("Frequency of letters:", freq_output)
# print("Sample Input 1: bob")
# format_output("bob")
# print("\nSample Input 2: marceal1bnnt0kakae")
# format_output("marceal1bnnt0kakae")