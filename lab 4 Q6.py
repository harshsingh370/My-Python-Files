#WAP to accept a string and count the frequency of each vowel
def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, 
                   "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    for char in string:
        if char in vowels:
            vowel_count[char] += 1
    for vowel, count in vowel_count.items():
        if count > 0:
            print(f"{vowel}: {count}")
input_string = input("Enter a string: ")
count_vowels(input_string)
