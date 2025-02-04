#WAP to demonstrate Slicing Operations in Strings
string = "Hello, World!"
print("Original string:", string)
substring1 = string[0:5]
print("Substring from index 0 to 4:", substring1)
substring2 =string[7:]
print("Substring from index 7 to the end:", substring2)
substring3 = string[:5]
print("Substring from the start to index 5:", substring3)
substring4 = string[-1]
print("Last character:", substring4)
substring5 = string[-5:]
print("Last 5 characters:", substring5)
substring6 = string[::2]
print("Every second character:", substring6)
substring7 = string[::-1]
print("Reversed string:",substring7)
