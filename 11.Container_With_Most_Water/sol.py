# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_id, right_id = 0, len(height)-1
        out = 0
        while left_id <= right_id:
            out = max(out, min(height[left_id], height[right_id]) * (right_id - left_id))
            if height[left_id] < height[right_id]:
                left_id += 1
            else:
                right_id -= 1
        return out
            
            
            
            
        
        
        
            
        
            
                
s = Solution()
print(s.maxArea([1, 100]))