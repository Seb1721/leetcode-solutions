"""
LeetCode 80: Remove Duplicates from Sorted Array II
# Date: 10/30/26
# Difficulty: Medium

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-
place such that each unique element appears at most twice. The relative order of the
elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must
instead have the result be placed in the first part of the array nums. More formally, if
there are k elements after removing the duplicates, then the first k elements of nums
should hold the final result. It does not matter what you leave beyond the first k
elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input
array in-place with O(1) extra memory.
"""

# Approach / Logic
    # Use a dictionary to iterate through nums and store each unique number as the key
    # and its number of occurrences as the value. Use two pointers to keep track of last
    # and next numbers. For each key in the dictionary

# Complexity
    # Time: O(n)
    # Space: O(1) -> because only new memory is i and k, and the data/operations do not
    #                grow with the nums.

# ======================================================================================
# Solution
# ======================================================================================
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # A list with 2 or fewer elements cannot have more than 2 identical nums
        if len(nums) <= 2:
            return len(nums)

        # Variable to represent the amount of valid entries in the list (ie. those that
        # do not appear more than twice)
        k = 2

        for i in range(2, len(nums)):
            # If the number in the current index does not equal the number in the index
            # two places before, add the number to the front of the original list nums.
            # This will keep the current ordering. If the current number does not match
            # the number at the index two jumps behind, then the count k is incremented
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k

# ======================================================================================
# Solution
# ======================================================================================
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     # Create empty dictionary to store the unique numbers as keys, and their count
    #     # as the values
    #     num_dictionary: dict[int, int] = {}
    #     final_list: list[int] = []
    #
    #     # Iterate through each element of list nums
    #     for n in nums:
    #         # Create dictionary entries for each unique key (digit) in nums. Initialize
    #         # to 0 if .get doesn't find the key in the dictionary. If the element is in
    #         # dictionary already, increment the value (count) by 1
    #         num_dictionary[n] = num_dictionary.get(n, 0) + 1
    #
    #         # If block to detect keys with a count of two or more
    #         if num_dictionary[n] <= 2:
    #             final_list.append(n)
    #
    #     nums[:] = final_list
    #
    #     return len(final_list)

# ======================================================================================
# Testing
# ======================================================================================

if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]),
    ]

    for nums, expected in tests:
        k = solution.removeDuplicates(nums)
        assert k == len(expected), f"k: got {k}, expected {len(expected)}"
        assert nums[:k] == expected, f"nums[:k]: got {nums[:k]}, expected {expected}"
    print("All tests passed")

# Notes
    # Two pointers, read/write: in-place filter or reduction, sorted input