# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        dct1 = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        lst = [1, 5, 10, 50, 100, 500, 1000]
        prev_lst = {5: 1, 10: 1, 50: 10, 100: 10, 500: 100, 1000: 100}
        def findclosest(num: int):
            m, prev = 0, 0
            for i in dct1.keys():
                if num - i >= 0 and num - i < num - m:
                    m = i
            if str(num)[0] in ['4', '9']:
                for i in lst:
                    if i > num:
                        m = i
                        prev = prev_lst[m]
                        break
            return m, prev

        temp = num
        out = ''
        while temp:
            m, prev = findclosest(temp)
            temp = temp - m + prev
            if prev:
                out += dct1[prev]
            out += dct1[m]
        return out
                
            
        
        
                
            
               
s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))