# 9/16/26
# Problem: Merge Sorted Array
# Difficulty: Easy

# Instructions:
    # You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    # and two integers m and n, representing the number of elements in nums1 and nums2
    # respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing
    # order. The array nums1 has a length of m + n where m denotes the elements to be
    # merged and the n represents elements after the m elements and should be set to 0.

# Logic:
    # M and N inputted. Append nums2 to nums1 starting at position m + 1. nums1 has n empty
    # spaces to fit n entries in nums2.

# Complexity:
    # Time: O((m + n) log(m + n))
    # Size:

# Solution
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m + j] = nums2[j]

        nums1.sort()
# Testing
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]

    solution.merge(nums1, m, nums2, n)

    print("Actual:  ", nums1)
    print("Expected:", expected)
    print("PASS" if nums1 == expected else "FAIL")

# Notes
"""
 Revisit with two-pointer solution
"""