s1 = input("Enter a word: ")
s2 = input("Enter another word: ")
if len(s1) != len(s2):
    print("Not an anagram")
else:
    for x in s1:
        if x not in s2:
            print("Not an anagram")
    else:
        print("Anagram")
