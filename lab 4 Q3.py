#WAP to check weather a given string is palindrome or not.
input_string = input("Enter a string: ")
final_string = input_string.replace(" ", "").lower()
if final_string == final_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
