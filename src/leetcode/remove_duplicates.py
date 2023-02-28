""" 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_indx = 0
        duplicate_indx = 0

        while duplicate_indx < len(nums):
            if nums[unique_indx] == nums[duplicate_indx]:
                duplicate_indx += 1
            else:
                unique_indx += 1
                nums[unique_indx] = nums[duplicate_indx]
        return unique_indx + 1


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    assert Solution().removeDuplicates(nums) == 3
    assert nums[:3] == [1, 2, 3]
