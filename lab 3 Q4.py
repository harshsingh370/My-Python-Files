#4. Write a python program to read three numbers and if any two variables are equal, print that number
num1 = int(input("Enter the first  number :  "))
num2 = int(input("Enter the second number : "))
num3  = int(input("Enter the third number : "))
if num1 == num2 ==  num3:
    print("All numbers are equal")
elif  num1 == num2:
    print("Number 1 is equal to Number 2")
elif num1 == num3:
    print("Number 1 is eual to Number 3")
elif num2 == num3:
    print("Number 2 s equal to Number 3")
else:
    print("All numbers are different")

           
           
