# WAP to display the smallest word from the string
input_string = input("Enter a string: ")
words = input_string.split()
smallest = words[0]
for word in words:
    if len(word) < len(smallest):
        smallest = word
print(f"The smallest word in the string is: {smallest}")
