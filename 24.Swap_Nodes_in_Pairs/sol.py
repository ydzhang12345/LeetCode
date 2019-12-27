# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        out = dummy = ListNode(0)
        dummy.next = head
        
        while (dummy.next and dummy.next.next):
            temp1 = dummy.next
            temp2 = dummy.next.next
            temp1.next = temp2.next
            temp2.next = temp1
            
            dummy.next = temp2
            dummy = temp1
        return out.next
        
        
            
    
        
               
s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
#l1.next.next.next = ListNode(4)



ss = s.swapPairs(l1)
while ss:
    print (ss.val)
    ss = ss.next

#print(s.mergeKLists([l1, l2, l3]))