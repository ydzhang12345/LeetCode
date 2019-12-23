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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        dummy2 = ListNode(0)
        dummy2.next = head
        count = 0
        while dummy.next:
            dummy = dummy.next
            count += 1
            if count>=n+1:
                dummy2 = dummy2.next
        if n==count:
            return head.next
        dummy2.next = dummy2.next.next
        return head
            
        
               
s = Solution()

ll = ListNode(1)
'''
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)
'''

print(s.removeNthFromEnd(ll, 2))