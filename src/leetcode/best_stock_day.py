from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_idx = 0
        r_idx = 1
        max_profit = 0

        while r_idx < len(prices):
            profit = prices[r_idx] - prices[l_idx]
            max_profit = max(max_profit, profit)
            if profit < 0:
                l_idx = r_idx
                r_idx += 1
            else:
                r_idx += 1

        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([2, 1, 4]))
    print(Solution().maxProfit([3, 2, 1]))
