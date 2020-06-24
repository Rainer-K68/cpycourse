!!! question "Lesson: Check palindromes"
    Create a function that
    
     - takes a single string argument
     - returns `True` if string is a palindrome, `False` otherwise
     - (1) Use a loop for implementation
     - (2) Try an alternative implementation using "extended slicing": Check 
     `word == word[::-1]` 
     - test the function by calling it with a palindrome-word and a 
    Optionally: Create a python script `check_palindrom.py` that asks the user
    to enter a word to be checked to be a palindrom
    
    ```
    python3 check_palindrom.py
    Please enter a word: abba
    word: abba - reversed-word: abba     # optional output
    is_palindrom: abba ==> True
    ```
    
    ```
    python3 check_palindrom.py
    Please enter a word: foo
    word: foo - reversed-word: oof       # optional output
    is_palindrom: foo ==> False
    ```
    
    Hint: use `input()`-builtin for user-input
        
    Optionally: Instead of user input provide a command line argument to your
    python script.
    
    Hint: Command line argument can be accessed using `sys.argv`.
