"""
Runtime: 40 ms, faster than 98.41% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.3 MB, less than 5.74% of Python3 online submissions for Merge Two Sorted Lists.
"""

"""
这种题居然没有一次性bug free
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(None)
        p = ret
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return ret.next
