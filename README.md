# Solutions

Question: Write a function that checks if a given word is a palindrome. Character case should be ignored.

Answer: For the above question, I have prepared the below mentioned logic:

def isPalindrome(word):
    word=word.lower();
    return word == word[::-1]
    
    
   That is, as character case should be ignored, so, I have converted the received word in lower cases. After that, I have used slicing operator with negative indexing in python to get the reverse of the same word and if it will be same as the original word then the provided word is palindrome else not.
   
