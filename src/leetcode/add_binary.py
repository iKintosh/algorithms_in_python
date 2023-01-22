"""
# 67. Add binary

The idea for this solution is not to use binary numbers in python
and try to create solution complitely based on strings and figure out
all possible cases we can face while adding up two binaries.

Otherwise the problem can be solved with oneliner.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        from_previous = "0"
        long_number = a if len(a) >= len(b) else b
        short_number = a if len(a) < len(b) else b
        
        result = []
        
        for i in range(1, len(short_number)+1):
            if sum(map(int, [long_number[-i], short_number[-i], from_previous])) == 3:
                result.append("1")
                from_previous = "1"
            elif sum(map(int, [long_number[-i], short_number[-i], from_previous])) == 0:
                result.append("0")
                from_previous = "0"
            elif sum(map(int, [long_number[-i], short_number[-i], from_previous])) == 2:
                result.append("0")
                from_previous = "1"
            elif sum(map(int, [long_number[-i], short_number[-i], from_previous])) == 1:
                result.append("1")
                from_previous = "0"
                
        for i in range(len(short_number)+1, len(long_number)+1):
            if sum(map(int, [long_number[-i], from_previous])) == 2:
                result.append("0")
                from_previous = "1"
            elif sum(map(int, [long_number[-i], from_previous])) == 1:
                result.append("1")
                from_previous = "0"
            elif sum(map(int, [long_number[-i], from_previous])) == 0:
                result.append("0")
                from_previous = "0"
            
        if from_previous != "0":
            result.append("1")
            
        result.reverse()
            
        return "".join(result)
        
            
            
    

if __name__ == "__main__":
    assert Solution().addBinary("11", "1") == "100"