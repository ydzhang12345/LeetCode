# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        if len(digits)>0:
            dct = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'], 
                   "5":['j','k','l'], "6":['m', 'n', 'o'], "7":['p','q','r','s'], 
                   "8":['t','u','v'], "9":['w','x','y','z']}
            def dfs(i, s):
                if i>=len(digits):
                    out.append(s)
                    return
                else:
                    for ch in dct[digits[i]]:
                        dfs(i+1, s+ch)
            
            dfs(0, '')
        return out
            
            
            
        
        
                
            
        
        
                
            
               
s = Solution()
print(s.letterCombinations("3"))