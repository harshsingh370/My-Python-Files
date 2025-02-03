#Write a python program to read three numbers and print them in ascending order (without using sort function)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2:
    num1, num2 = num2, num1  
if num2 > num3:
    num2, num3 = num3, num2  
if num1 > num2:
    num1, num2 = num2, num1  
print("Numbers in ascending order:", num1,num2,num3)
