# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List, Tuple, Dict, TextIO
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        a, b = 0, 1
        while (b<len(nums)):
           if nums[a]==nums[b]:
               nums.pop(b)
           else:
               a += 1
               b += 1
        print(nums)
        return len(nums)
        
          
s = Solution()
print(s.removeDuplicates([1,1,2,2,3,4,5]))