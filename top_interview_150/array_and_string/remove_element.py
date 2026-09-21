# ======================================================================================
# Problem Information
# ======================================================================================
# Date: 9/21/26
# Problem Number: 27
# Problem Name: Remove Element
# Difficulty: Easy


# ======================================================================================
# Instructions
# ======================================================================================
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums
in-place. The order of the elements may be changed. Then return the number of elements
in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get
accepted, you need to do the following things:
    --> Change the array nums such that the first k elements of nums contain the
    elements which are not equal to val. The remaining elements of nums are not
    important as well as the size of nums.
    --> Return k
"""

# ======================================================================================
# Approach / Logic
# ======================================================================================
#
"""
Iterate through nums with a read pointer. As you go, check whether or not each entry
matches the given integer val with a for loop. If not, reassign the int you're processing
to the index of a separate write pointer in the original list nums. This way, only valid
integers are kept and reassigned to the beginning of nums in place. Increment the write
pointer each time a valid int is reassigned into nums. Return the write pointer because
it represents the number of valid integers, k.
"""

# ======================================================================================
# Complexity
# ======================================================================================
# Time: O(n) --> Every element processed once
# Space: O(1) --> Modifies nums in place and creates a few vars

# ======================================================================================
# Solution
# ======================================================================================
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_index = 0

        for num in nums:
            if num != val:
                nums[write_index] = num
                write_index += 1

        k = write_index
        return k

# ======================================================================================
# Testing
# ======================================================================================
if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    expected_nums = [2, 2]
    expected_k = 2

    actual_k = solution.removeElement(nums, val)

    print("Actual k:    ", actual_k)
    print("Expected k:  ", expected_k)
    print("Actual nums: ", nums[:actual_k])
    print("Expected nums:", expected_nums)
    print("PASS" if actual_k == expected_k and nums[:actual_k] == expected_nums else "FAIL")

# ======================================================================================
# Notes
# ======================================================================================
"""
Definitely retry without any assistance. Work on recognizing using indices as makeshift
pointers when necessary.
"""
