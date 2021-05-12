def isPalindrome(word):
    word=word.lower();
    return word == word[::-1]
 
s=input("Enter a word\n")
ans = isPalindrome(s)
 
if ans:
    print("The Given word is palndrome")
else:
    print("The Given Word is not palindrome")
