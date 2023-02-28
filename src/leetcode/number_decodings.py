# class Solution:
#     def numDecodings(self, s: str) -> int:
#         len_s = len(s)
#         dec = [0] * (len_s + 1)
#         dec[0] = 1
#         dec[1] = 1  # possibilities to decode s[0] symbol
#         if s[0] == "0":
#             return 0
#         for i in range(2, len_s + 1):
#             if 1 <= int(s[i - 1]) <= 9:
#                 dec[i] += dec[i - 1]
#             if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
#                 dec[i] += dec[i - 2]
#             print(dec)
#         return dec[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dict()
        self._recursive(s, dp)
        print(dp)
        return dp[s]

    def _recursive(self, s: str, dp: dict) -> int:
        print(s, dp, s[:1], s[:2])
        if not s:
            return 1
        if s in dp:
            return dp[s]
        first, second = 0, 0
        if 1 <= int(s[:1]) <= 9:
            first = self._recursive(s[1:], dp)
        if 10 <= int(s[:2]) <= 26:
            second = self._recursive(s[2:], dp)
        dp[s] = first + second
        print(s, dp, s[:1], s[:2])
        print()
        return dp[s]


if __name__ == "__main__":
    # print(Solution().numDecodings("123"))
    # print(Solution().numDecodings("0"))
    print(Solution().numDecodings("123"))
