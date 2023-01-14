import re

# # Search for capital letters
# pattern = re.compile("^[A-Za-z\s]+")

# # Search checks the whole string even if it doesn't match at the start
# print(pattern.search("hello world"))
# print(pattern.search("HELLO WORLD"))
# print(pattern.search("helloworld"))
# print(pattern.search("HelloWorld"))

# # Match checks for at the start if the string for any matching characters
# print(pattern.match("hello world"))
# print(pattern.match("HELLO WORLD"))
# print(pattern.match("helloworld"))
# print(pattern.match("HelloWorld"))



# Example 
# 3 lowercase letters
# 3-5 digits
# One symbol
# 2 uppercase (optional)
# pat = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")

# print("Example")
# print(pat.search("llo1223T#AJ"))
# print(pat.search("ahd323#A"))
# print(pat.search("helloworld"))
# print(pat.search("HelloWorld"))

# def checker(string):
#     pattern2 = re.compile("^[a-z\s]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0-2}$")
#     if pattern2.search(string) == "None":
#         print(f"The string {string} did not match the regex exppr")
#     print(f"The string {string} matshed")
    
# finding certain number of characters
def ten_character_regex(string: str) -> str:
    pattern = re.compile("^.{10}$")
    print(pattern.search(string))
    
# ten_character_regex("stringedsd") # -> <re.Match object; span=(0, 10), match='stringedsd'>
# ten_character_regex("string") # -> None
    
    
    
# Validating email
def email_validate_regex(email: str) -> str:
    pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9\-]+\.{1}[a-zA-Z]{2,4}$")
    print(pattern.search(email))

email_validate_regex("admin@captainkite.tech")
email_validate_regex("admin@captain-kite.smart")
email_validate_regex("admin@captain-kite.tech")
email_validate_regex("ad_--min@captainkite.tech")
