# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr, rl, out = [], [], []
        templ, tempr = 1, 1
        for i in range(len(nums)):
            templ = templ * nums[i]
            tempr = tempr * nums[-i-1]
            lr.append(templ)
            rl.append(tempr)
        for i in range(len(nums)):
            out.append(1)
            if i > 0:
                out[-1] *= lr[i-1]
            if i < len(nums) - 1:
                out[-1] *= rl[len(nums)-1-i-1]
        return out
            
        
            
                
s = Solution()
print(s.productExceptSelf([3,4]))