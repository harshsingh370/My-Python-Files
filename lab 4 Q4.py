#WAP to capitalize the first and last character of each word in a string.
string = input("Enter a string: ")
words = string.split()  
result = []
for word in words:
    if len(word) == 1:
        result.append(word.upper())  
    else:
        result.append(word[0].upper() + word[1:-1] + word[-1].upper())  
print("Transformed string:", ' '.join(result))
 
