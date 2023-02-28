"""153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l_idx = 0
        r_idx = len(nums) - 1

        while l_idx < r_idx:
            mid = int((l_idx + r_idx) / 2)  # type: ignore
            if nums[l_idx] > nums[r_idx]:
                if nums[mid] > nums[r_idx]:
                    l_idx = mid + 1
                else:
                    r_idx = mid
            else:
                if nums[mid] >= nums[l_idx]:
                    r_idx = mid
        return nums[r_idx]


if __name__ == "__main__":
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([11, 13, 15, 17, 0]) == 0
