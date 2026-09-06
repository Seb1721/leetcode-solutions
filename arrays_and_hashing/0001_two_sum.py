from typing import List

# 8/27/26
# Problem 1: Two Sum
# Difficulty: Easy

# Instructions:
    # You are given an array of integers nums and an integer target. Return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.

# Logic:
    # Brute force method: go through every possible number pair in the array using 2 for loops, inner and outer.
    # Efficient method: create a hashmap where keys are numbers and values are their indices. Create a variable
    # named 'complement' to store the number needed to reach the target. Store each seen number in the dictionary
    # named 'seen'.

# Complexity:
    # Time: O(n)
    # Size: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store each previously seen number and its index.
        seen = {}

        # Loop through nums using enumerate to get each index and number.
        # ie: Loop through each (index, number) tuple made from enumerate(nums)
        for index, number in enumerate(nums):
            # Calculate the number needed to reach the target.
            complement = target - number

            # If the complement is already in seen, return the previous index and current index.
            if complement in seen:
                return [seen[complement], index]

            # Store the current number as the key and its index as the value.
            seen[number] = index

        return []
