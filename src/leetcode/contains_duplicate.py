from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup_dict = {}
        for i in nums:
            if lookup_dict.get(i) != None:
                return True
            else:
                lookup_dict[i] = 1
        return False
    
    
if __name__ == "__main__":
    assert Solution().containsDuplicate([1,2,3,4]) == False
    assert Solution().containsDuplicate([1,2,3,1]) == True