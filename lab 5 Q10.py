# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
my_string = input("Enter a string: ")

if len(my_string) >= 3:
    if my_string.endswith("ing"):
        my_string += "ly"
    else:
        my_string += "ing"
        
print("Modified string:", my_string)
