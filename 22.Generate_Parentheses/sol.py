# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = set()
        left, right, s = 0, 0, ''
        
        def dfs(l, r, s):
            if l==n and r==n:
                out.add((s))
            if l < n:
                dfs(l+1, r, s+'(')
            if r < l:
                dfs(l, r+1, s+')')
        dfs(left, right, s)
        return out
                
                
            
            
        
            
        
               
s = Solution()

print(s.generateParenthesis(0))