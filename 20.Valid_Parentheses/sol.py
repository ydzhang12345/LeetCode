# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if len(stack) < 1:
                    return False
                if i==")" and stack[-1]=="(":
                    stack.pop()
                    continue
                if i=="}" and stack[-1]=="{":
                    stack.pop()
                    continue
                if i=="]" and stack[-1]=="[":
                    stack.pop()
                    continue
                return False
        if len(stack) > 0:
            return False
        return True
        
            
        
               
s = Solution()

print(s.isValid(']'))