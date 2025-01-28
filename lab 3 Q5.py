#5. Write a python program to read three numbers and find the smallest among them
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number : "))
smallest = num1
if (num2<num1 and num2<num3):
    print("second number is smallest : ",num2)
elif (num3<num1 and num3<num2):
    print("third number is smallest : ",num3)
else:
    print("first numer is smallest: ",num1)
    
