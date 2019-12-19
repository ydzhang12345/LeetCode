# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pdb

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        ch_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p)>=2 and p[1]=='*':
            return (self.isMatch(s, p[2:])) or (ch_match and self.isMatch(s[1:], p))
        else:
            return ch_match and self.isMatch(s[1:], p[1:])
        
            
        
            
    
s = Solution()
print(s.isMatch("aaa", "ab*a*c*a"))