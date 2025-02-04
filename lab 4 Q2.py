#WAP to demonstrate built in functions of Strings.
string = "Hello, World! This was my first program."
print("Original string:", string)
print("Length of the string:", len(string))
print("Lowercase string:", string.lower())
print("Uppercase string:",string.upper())
print("Capitalized string:", string.capitalize())
print("Title case string:", string.title())
print("String with 'World' replaced by 'Universe':", string.replace("World", "Universe"))
print("List of words in the string:", string.split())
print("Occurrences of 'o':", string.count('o'))
