# Write a Python program to count the number of characters (character frequency) in a string.
my_string = input("Enter a string: ")
char_count = {}
for char in my_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character frequency:", char_count)
