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

'''
O(NK)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        out = ListNode(0)
        out.next = dummy
        
        while (1):
            flag = False
            minn = float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minn:
                    minn = lists[i].val
                    idx = i
            if minn==float('inf'):
                break
            lists[idx] = lists[idx].next
            dummy.next = ListNode(minn)
            dummy = dummy.next
            
        return out.next.next
'''

# maintain a priorityQueue with length of K
# O(NlogK)
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = dummy = ListNode(0)
        q = PriorityQueue()
        idx = 0
        for l in lists:
            if l:
                idx += 1
                q.put((l.val, idx, l))
        
        while not q.empty():
            val, _, node = q.get()
            dummy.next = ListNode(val)
            dummy = dummy.next
            node = node.next
            if node:
                idx += 1
                q.put((node.val, idx, node))
        return head.next
            
            
        
            
        
               
s = Solution()

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)


ss = s.mergeKLists([l1, l2, l3])
while ss:
    print (ss.val)
    ss = ss.next

#print(s.mergeKLists([l1, l2, l3]))