from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        effective_k = k % len_nums

        print(nums)
        nums[len_nums - effective_k :] = self.reverse(nums[len_nums - effective_k :])
        print(nums)
        nums[: len_nums - effective_k] = self.reverse(nums[: len_nums - effective_k])
        print(nums)
        nums[:] = self.reverse(nums[:])
        print(nums)

    def reverse(self, nums) -> List[int]:
        l_idx = 0
        r_idx = len(nums) - 1

        while l_idx < r_idx:
            nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
            l_idx += 1
            r_idx -= 1

        return nums


if __name__ == "__main__":
    Solution().rotate([1, 2, 3, 4], 2)
