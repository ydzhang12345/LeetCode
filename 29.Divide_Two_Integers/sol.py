# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List, Tuple, Dict, TextIO
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        toggle = -1 if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0
        while True:
            temp = divisor
            q = 1
            if dividend < temp:
                break
            while dividend - temp - temp > 0:
                temp += temp
                q += q
            dividend -= temp
            count += q
        return max(-2147483648, min(count * toggle, 2147483647))
        
            
            
            
        
        
          
s = Solution()
print(s.divide(99, 2))