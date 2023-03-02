from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        max_sum = 0
        for day in price_diff:
            if day > 0:
                max_sum += day

        return max_sum


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
