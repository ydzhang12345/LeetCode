# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = 1e9
        print(nums)
        for i in range(1, len(nums)-1):
            l = 0
            r = len(nums) - 1

            while l < i and r > i :
                summ = nums[i] + nums[l] + nums[r]            
                if summ == target:
                    return target
                if abs(summ-target) < abs(m-target):
                    m = summ             
                if summ < target:
                    l += 1
                else:
                    r -= 1
        return m
                
            
               
s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))