# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List, Tuple, Dict, TextIO
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        for i in range(len(haystack) - len(needle)+1):
            if needle==haystack[i:i+len(needle)]:
                return i
        return -1
        
        
          
s = Solution()
print(s.strStr("a", "a"))