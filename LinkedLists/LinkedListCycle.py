# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Question: https://leetcode.com/problems/linked-list-cycle/description/
# Solution: Floyd's Cycle Detection
# Use two pointers - move them with different pace one with say 1 node
# and other with 2 nodes.


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 and p2 and p1 == p2:
                return True

        return False