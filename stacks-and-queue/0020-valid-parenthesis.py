# 9/3/26
# Problem 20: Valid Parenthesis
# Difficulty: Easy

# Instructions:
    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    # An input string is valid if:
    #   Open brackets must be closed by the same type of brackets.
    #   Open brackets must be closed in the correct order.
    #   Every close bracket has a corresponding open bracket of the same type.

# Logic:
    # Create a stack to track open parenthetical chars in string s. As the string is procesed, track opening
    # parenthesis and ensure that the next closing character matches with the last opener. If string is
    # an uneven number of chars, return false. If the opening and closing parentheticals dont match 
    # for the pop, return false. 

# Complexity:
    # Time:
    # Size:

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack implemented as a List in python. pop() returns the last item in the list.
        # Store each char in s in a List/Stack
        bracket_stack = []
        last_opening_char = None
        # Create a small dictionary to set acceptable pairs of opening/closing brackets
        # Closing brackets are keys, opening are values
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        # First if length of string is odd, return False
        if len(s) % 2 != 0:
            return False
        # For each char in the string ...
        for char in s:
            # If char is an opening bracket, add it to bracket_stack
            if char in "([{":
                bracket_stack.append(char)
            # Else, the char is a closing bracket, so check validity of placement
            else:
                # Safeguard against popping empty stack
                if not bracket_stack:
                    return False
                # Pop the stack to assign the last opening char
                last_opening_char = bracket_stack.pop()
                # Compare last opening char to the dict result of current char in pairs dict.
                # If the current char's dict lookup in pairs doesn't match last_opening_char, return False.
                if last_opening_char != pairs[char]:
                    return False
        # If the stack is empty, return true, if not empty return false.
        return not bracket_stack
