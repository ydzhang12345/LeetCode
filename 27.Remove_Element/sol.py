# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List, Tuple, Dict, TextIO
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except Exception:
                break
        return len(nums)
        
        
          
s = Solution()
print(s.removeElement([1,1,2,2,3,4,5], 1))