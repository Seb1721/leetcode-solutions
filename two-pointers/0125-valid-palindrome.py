# 8/27/26
# Problem 125: Valid Palindrome
# Difficulty: Easy

# Instructions:
    # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
    # removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
    # characters include letters and numbers.
    # 
    # Given a string s, return true if it is a palindrome, or false otherwise.

# Logic:
    # First, convert the string to a cleaned form with alphanumeric characters only.
    # Find and set indices of beginning and end of string equal to begin and end variables. As you iterate
    # towards the middle, the value in each index should be the same for the front and back 'pointers'. 
    # If the values do not match at any point, return False, otherwise, return True.

# Complexity:
    # Time: O(n) --> maximum n characters processed once 
    # Size: O(n) --> maximum n characters in string 

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # First create a variable to hold the 'cleaned up' string: alphanumeric only 
        cleanString = ''.join(char.lower() for char in s if char.isalnum())

        # Create varables to save the index of the front and back characters in the stirng.
        frontIndex = 0
        backIndex = len(cleanString) - 1

        # Create a variable to store the number of iterative steps
        numSteps = len(cleanString) // 2

        # Works with both even and odd --> single midddle character can't ruin a palindrome
        for i in range(numSteps):
            if cleanString[frontIndex] == cleanString[backIndex]:
                frontIndex += 1
                backIndex -= 1
            else: 
                return False
        return True