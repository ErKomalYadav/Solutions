# Solutions

###### Problem No:02: Write a function that checks if a given word is a palindrome. Character case should be ignored.

Answer: For the above question, I have prepared the below mentioned logic:

def isPalindrome(word):
    word=word.lower();
    return word == word[::-1]
    
    
   That is, as character case should be ignored, so, I have converted the received word in lower cases. After that, I have used slicing operator with negative indexing in python to get the reverse of the same word and if it will be same as the original word then the provided word is palindrome else not.
   
### Problem No: o3.

The Logics implemented for this are mentioned below:

The logging module provides us with a default logger that allows you to get started without needing to do much configuration. so, I have used logging module of python to make the things easier.Also, we can display our warning and error messages in seperate file, as:

logging.basicConfig(filename='komal.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s').

### Problem No: 04:

As we know,
cd .. will move the user up one directory. So, if they are /a/b/c/d, cd .. moves them to /a/b/c, while cd ../x moves them to /a/b/c/x. The user can use this indirection to access subdirectories too. So,the same logic is implemented with the help of different required functions in c# which finally returns our required output.






