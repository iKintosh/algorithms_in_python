"""11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx = 0
        r_idx = len(height) - 1
        area = 0

        while l_idx < r_idx:
            new_area = (r_idx - l_idx) * min(height[l_idx], height[r_idx])
            area = max(area, new_area)
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        return area


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
