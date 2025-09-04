'''Write a program to find check if a string has only octal digits. Given string
['789', '123', '004']'''
# import re
# str_list = ['789', '123', '004']
# pattern = r'^[0-7]+$'
# for s in str_list:
#     if re.fullmatch(pattern, s):
#         print(f"'{s}' contains only octal digits.")
#     else:
#         print(f"'{s}' does NOT contain only octal digits.")

'''Extract the user id, domain name and suffix from the following email addresses.
emails =
"""zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
'''
# import re
# emails = """zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com"""
# pattern = r'(\w+)@(\w+)\.(\w+)'
# matches = re.findall(pattern, emails)
# for user_id, domain, suffix in matches:
#     print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")

'''Split the following irregular sentence into proper words
sentence = """A, very very; irregular_sentence""" ## expected output: A very very irregular sentence'''
# import re
# sentence = "A, very very; irregular_sentence"
# words = re.split(r'[^a-zA-Z]+', sentence)
# result = ' '.join(filter(None, words))
# print(result)

'''Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxod cc: @garybernhardt #rstats"
##desired_output = 'Good advice What I would do differently if I was learning to code today'
'''
# import re
# tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxod cc: @garybernhardt #rstats"
# tweet = re.sub(r'\b(RT|cc)\b:? ?', '', tweet, flags=re.IGNORECASE)
# tweet = re.sub(r'@\w+', '', tweet)
# tweet = re.sub(r'http\S+', '', tweet)
# tweet = re.sub(r'#\w+', '', tweet)
# tweet = re.sub(r'[^\w\s]', '', tweet)
# tweet = re.sub(r'\s+', ' ', tweet).strip()
# print(tweet)

'''
Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Code to retrieve the HTML page is given below:
import requests
r =
requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
'''
# import requests
# from bs4 import BeautifulSoup
# url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
# r = requests.get(url)
# html = r.text
# soup = BeautifulSoup(html, 'html.parser')
# text_list = []
# for text in soup.stripped_strings:
#     text_list.append(text)
# print(text_list)

'''
Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as
'''
# words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
# result = [word for word in words if word[0] == word[-1]]
# print(result)
