"""https://leetcode.com/problems/missing-number/"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        sum_len = sum([i for i in range(len_nums + 1)])
        sum_nums = sum(nums)
        return sum_len - sum_nums
