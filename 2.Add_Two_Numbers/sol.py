import pdb

# a clever use of ListNode

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
    	rightshift = 0
    	root = n = ListNode(0)
    	while l1 or l2 or rightshift:
    		v1 = v2 = 0
    		if l1:
    			v1 = l1.val
    			l1 = l1.next
    		if l2:
    			v2 = l2.val
    			l2 = l2.next
    		rightshift, val = divmod(v1 + v2 + rightshift, 10)
    		n.next = ListNode(val)
    		n = n.next
    	return root.next

sol = Solution()
r1 = ListNode(1)
r1.next = ListNode(1)
r1.next.next = ListNode(1)

r2 = ListNode(9)
r2.next = ListNode(8)
r2.next.next = ListNode(8)


r = sol.addTwoNumbers(r1, r2)
print(r.val)
while r.next is not None:
	r = r.next
	print(r.val)




