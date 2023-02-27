class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ = self.apply_backspace(s)
        t_ = self.apply_backspace(t)
        return s_ == t_

    def apply_backspace(self, old_str: str) -> str:
        new_str = []
        backspace = 0
        for sym in reversed(list(old_str)):
            if sym == "#":
                backspace += 1
            elif backspace == 0:
                new_str.append(sym)
            else:
                backspace -= 1
                continue
        return ''.join(reversed(new_str))
    
    
if __name__ == "__main__":
    assert Solution().backspaceCompare("ab#c", "ad#c") == True
    assert Solution().backspaceCompare("a#c", "b") == False
    assert Solution().backspaceCompare("ab##", "c#d#") == True