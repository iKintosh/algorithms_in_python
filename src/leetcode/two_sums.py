"""1. Two Sum
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_canditates = {}
        for i in range(len(nums)):
            if nums[i] in dict_canditates:
                return [dict_canditates[nums[i]], i]
            needed = target - nums[i]
            dict_canditates[needed] = i
        return []
