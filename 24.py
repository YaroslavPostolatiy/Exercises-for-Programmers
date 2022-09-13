# №24

print("Enter two strings and I'll tell you if they are anagrams:")

first_word = str(input("Enter the first string:"))
second_word = str(input("Enter the second string:"))

if sorted(first_word) == sorted(second_word):
    print(f"{first_word} and {second_word} are anagrams.")
else:
    print(f"{first_word} and {second_word} aren`t anagrams.")
    