#WAP to accept two strings from the user and display the common words.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
set1 = set(str1.split())
set2 = set(str2.split())
common_words = set1.intersection(set2)
if common_words:
    print("Common words:", ' '.join(common_words))
else:
    print("No common words found.")
