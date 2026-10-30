"""
LeetCode 26: Remove Duplicates from Sorted Array
# Date: 10/29/26
# Difficulty: Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-
place such that each unique element appears only once. The relative order of the
elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates,
return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The
remaining elements beyond index k - 1 can be ignored.
"""

# Approach / Logic
    # Create a dictionary to hold each unique number as the key. Python dictionaries
    # save items in the order they are stored in, so the relative order should be kept.
    # Return the number of items in the dictionary.

# Complexity
    # Time: O(n)
    # Space: O(n)

# ======================================================================================
# Solution
# ======================================================================================
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Create empty dictionary to store the unique numbers
        seen_nums: dict[int, None] = {}

        # Update the dictionary for each number in the original list. fromkeys(iter)
        # creates a dictionary and assigns keys with the same value from an iterable
        # object.
        #
        # Here, each unique key (number) is added. Update overwrites key/value pairs
        # and keeps the relative order intact, meaning only one of every number will
        # be kept.
        seen_nums.update(dict.fromkeys(nums))
        nums[:] = seen_nums

        return len(seen_nums)

    # Alternative Sol

        # Approach / Logic
            # Can use the fact that the list is sorted to your advantage. Last num and
            # next num pointer can be used to determine whether a number should be added
            # as identical numbers will be adjacent to each other and can be easily
            # skipped.

    # class Solution:
    #     def removeDuplicates(self, nums: list[int]) -> int:
    #         if not nums:
    #             return 0
    #
    #         # The first element is always unique, so the write pointer starts at 1
    #         k = 1
    #
    #         for i in range(1, len(nums)):
    #             # Compare against the last unique value kept, not nums[i - 1], which may
    #             # already have been overwritten
    #             if nums[i] != nums[k - 1]:
    #                 nums[k] = nums[i]
    #                 k += 1
    #
    #         return k

# ======================================================================================
# Testing
# ======================================================================================
if __name__ == "__main__":
    solution = Solution()

    # Add test cases here.

# Notes