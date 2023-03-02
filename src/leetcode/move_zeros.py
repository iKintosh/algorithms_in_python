"""Move zeros.
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_idx = 0
        for elem in nums:
            if elem != 0:
                nums[last_non_zero_idx] = elem
                last_non_zero_idx += 1
        for i in range(last_non_zero_idx, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    nums = [0, 0, 1, 0]
    Solution().moveZeroes(nums)
    assert nums == [1, 0, 0, 0]
