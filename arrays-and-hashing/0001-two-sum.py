# 8/27/26
# Problem 1: Two Sum
# Difficulty: Easy

# Instructions:
    # You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.

# Logic:
    # Brute force method: go through every possible number pair in the array using 2 for loops, inner and outer.
    # Efficient method: create a hashmap, keys are the numbers and values are their indices. Create a variable 
    # named 'complement' to store the complement of the number that's currently being iterated. Store 'seen'
    # nums in the dictionary 'seen'.

# Complexity:
    # Time: O(n)
    # Size: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store each previously seen number and its index.
        seen = {}

        # Loop through nums, getting both the index and number.
        for index, number in enumerate(nums):
            # Calculate the number needed to reach the target.
            complement = target - number

            # If that number was previously seen, return both indices.
            if complement in seen:
                return [seen[complement], index]

            # Store the current number as the key and its index as the value.
            seen[number] = index