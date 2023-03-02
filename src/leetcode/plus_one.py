from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r_digits = list(reversed(digits))
        inc = 1
        i = 0
        while inc != 0:
            if i < len(r_digits):
                r_digits[i], inc = (r_digits[i] + inc) % 10, (r_digits[i] + inc) // 10
            else:
                r_digits.append((inc) % 10)
                inc = inc // 10
            i += 1
        digits = list(reversed(r_digits))
        return digits
