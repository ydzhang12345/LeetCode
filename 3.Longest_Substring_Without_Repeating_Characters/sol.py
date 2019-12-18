# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid_len = (m + n) // 2 + (m + n) % 2
        
        # binary search to find how much elements from nums1 should contribute 
        # to the final sorted sequence
        left = max(0, mid_len - n)
        right = min(mid_len, m);
        while (left <= right):
            # mid_temp1 elements are picked from nums1
            mid_temp1 = min((left + right) // 2, m)
            # mid_temp2 elements are picked from nums2
            mid_temp2 = min(mid_len - mid_temp1, n)
            
            # validate the resulting array
            if mid_temp2-1<0 or (mid_temp1-1>=0 and nums1[mid_temp1-1] >= nums2[mid_temp2-1]):
                if n<=mid_temp2 or nums1[mid_temp1-1] <= nums2[mid_temp2]:
                    if (m+n)%2==1:
                        median = nums1[mid_temp1-1]
                    else:
                        if m>mid_temp1:
                            next_1 = nums1[mid_temp1]
                        else:
                            next_1 = 1e9
                        if n>mid_temp2:
                            next_2 = nums2[mid_temp2]
                        else:
                            next_2 = 1e9                            
                        median = (nums1[mid_temp1-1] + min(next_1, next_2))/2                        
                    return median*1.0
                else:
                    right = mid_temp1-1
            else:
                if m<=mid_temp1 or nums2[mid_temp2-1] <= nums1[mid_temp1]:
                    if (m+n)%2==1:
                        median = nums2[mid_temp2-1]
                    else:
                        if m>mid_temp1:
                            next_1 = nums1[mid_temp1]
                        else:
                            next_1 = 1e9
                        if n>mid_temp2:
                            next_2 = nums2[mid_temp2]
                        else:
                            next_2 = 1e9
                        median = (nums2[mid_temp2-1] + min(next_1, next_2))/2                        
                    return median*1.0
                else:
                    left = mid_temp1+1
                
s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))