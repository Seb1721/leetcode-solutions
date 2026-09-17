# 8/27/26
# Problem 217: Contains Duplicates
# Difficulty: Easy

# Instructions:
    # Given an integer array nums, return true if any value appears at least twice in the array, and 
    # return false if every element is distinct.

# Logic:
    # Make a hashmap of the integers in the list, with key being the number and value being the index.
    # Loop through each element of the 'seen' hashmap. if the keys of any two entries match, return false.

# Complexity: 
    # Time: O(n)
    # Size: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create empty set
        seen = set()

        # Repeat for each number in list 'nums'...
        for number in nums:
            # Check if the number is already in set 'seen', and if so return true and exit loop/program.
            if number in seen:
                return True
            # If the number has not already been added to 'seen', add it now.
            seen.add(number)
        # If there are no matches in seen and all nums have been processed, return false.
        return False
