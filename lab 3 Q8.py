#Write a python program to read a number, if it is an even number , print the square of that number and if it is odd number print cube of that number
num = int(input("Enter a number: "))
if num % 2 == 0:
    result = num ** 2  
    print(f"The number is even. Square: {result}")
else:
    result = num ** 3  
    print(f"The number is odd. Cube: {result}")
