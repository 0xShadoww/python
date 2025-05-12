#2nd skill testing 
#word checker
#cooking time

#input
word = input("Type your word: ");

#print
print("Number of characters: " ,len(word));

#checks
if ("a" in word) or ("e" in word) or ("i" in word) or ("o" in word) or ("u" in word):
    print("contains vowels: yes");
else:
    print("contains vowels: No");
if word == word[::-1]:
    print("Is a palindrome: Yes")
else:
    print("Is a palindrome: No")
