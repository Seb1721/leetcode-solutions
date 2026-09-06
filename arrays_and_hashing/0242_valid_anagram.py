# 8/27/26
# Problem 242: Valid Anagram
# Difficulty: Easy

# Instructions:
    # Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Logic:
    # First, compare length of the strings as anagrams must have an equal amout of characters. 
    # If length is equal, process each character in s and store them in dictionary as a key, and their frequency as the value.
    # Each time a new letter is processed, check them against characters in 'seen' dictionary. If they match any char, keep track of 
    # their frequency by incrementing the value in the K/V pair.   

# Complexity:
    # Time: O(n)
    # Size: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of the two strings don't match, they cannot possibly be anagrams.
        if len(s) != len(t):
            return False

        seenLetters_S = {}
        seenLetters_T = {}

        # For each letter in the string 's' starting with s[0]
        for letter in range(len(s)):
            # In each iteration, first check if letters in string 's' exists in seenLetters
            if s[letter] in seenLetters_S:
                # Increment value by 1 to count repeated letters
                seenLetters_S[s[letter]] += 1
            else:
                # If letter is not in seenLetters, add and set count to 1
                seenLetters_S[s[letter]] = 1

        # For each letter in the string 't' starting with t[0]
        for letter in range(len(t)):
            # In each iteration, first check if letters in string 't' exists in seenLetters
            if t[letter] in seenLetters_T:
                # Increment value by 1 to count repeated letters
                seenLetters_T[t[letter]] += 1
            else:
                # If letter is not in seenLetters, add and set count to 1
                seenLetters_T[t[letter]] = 1

        # Compare the two dictionaries. Return True if equal, False if not
        if seenLetters_S == seenLetters_T:
            return True
        else:
            return False
        