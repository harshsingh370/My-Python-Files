# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Swap the first two characters of both strings
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

result = new_str1 + ' ' + new_str2
print("Result:", result)
