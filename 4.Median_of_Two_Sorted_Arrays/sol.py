# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dct = {}
        mem = {}
        maxx = 0
        
        if len(s)<=1:
            return s
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]]=[i]
            else:
                dct[s[i]].append(i)
            mem[(i,i)] = 1
            if i < len(s) - 1:
                mem[(i, i+1)] = int(s[i]==s[i+1])
        maxx = 1
        left = 0
        right = 0
        
        def dfs(i, j) -> int:
            if s[i]!=s[j]:
                return 0
            if i>j:
                return 1
            if (i,j) in mem:
                return mem[(i,j)]
            mem[(i, j)] = dfs(i+1, j-1)
            return mem[(i, j)] 
        
        for i in range(len(s)):
            d = dct[s[i]]
            for j in d[::-1]:
                if i!=j and j>i:
                    #if j-i==1:
                    #    mem[(i,j)] = 2
                    if j - i + 1 >= maxx:    
                        mem[(i,j)] = dfs(i+1, j-1) * (j-i+1)           
                        if mem[(i, j)] > maxx:
                            maxx = mem[(i,j)]
                            left = i
                            right = j
        
        return s[left:right+1]
                # check if i to j-1 can be palindromic
                
            
                
s = Solution()
print(s.longestPalindrome("abcba"))