"""238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # type: ignore
        len_nums = len(nums)
        ans = [1] * len_nums
        prefix = 1
        postfix = 1

        for i in range(len_nums):
            ans[i] *= prefix
            prefix *= nums[i]
            ans[len_nums - i - 1] *= postfix
            postfix *= nums[len_nums - i - 1]
        return ans


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
