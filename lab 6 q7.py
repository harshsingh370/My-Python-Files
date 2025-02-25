# Write a Python program to remove duplicates from a list
x = [3, 5, 4, 3, 9, 0, 9]
i = 0
while i < len(x):
    j = i + 1
    while j < len(x):
        if x[i] == x[j]:
            del x[j]
        else:
            j += 1
    i += 1

print(x)
