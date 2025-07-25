import re

# 2. re.search() - Checks if the pattern exists anywhere in the string

text = "I love Python"
result = re.search("Python", text)
print(result)  # Match object if found, else None

# 3. re.match() - Checks if the pattern matches at the beginning of the string

text = "Python is great"
result = re.match("Python", text)
print(result)  # Match object if found at start

# re.findall() - Returns all matches as a list

text = "Python is easy. Python is powerful."
result = re.findall("Python", text)
print(result)  # ['Python', 'Python']

# re.sub() - Replaces occurrences of the pattern with a replacement string

text = "I love Python"
result = re.sub("Python", "Java", text)
print(result)  # I love Java

# re.split() - Splits a string by the pattern

text = "apple,banana,grapes"
result = re.split(",", text)
print(result)  # ['apple', 'banana', 'grapes']

# Example: Match Email

email = "my email is test@example.com"
pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.(com|org)"
match = re.search(pattern, email)
print(match.group())  # test@example.com

# Example: Match Phone Number

phone = "Call me at 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"  # Matches phone number format
match = re.search(pattern, phone)
if match:
    print("Phone number found:", match.group())  # 123-456-7890
else:
    print("No phone number found")

# Example: Match URL
url = "Visit us at https://www.example.com"
pattern = r"https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+"
match = re.search(pattern, url)         
if match:
    print("URL found:", match.group())  # https://www.example.com