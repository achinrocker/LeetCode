# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Question: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Solution Approach
# Maintain two pointers p1 and p2 initialized at the head of A and B, respectively.
# Then let them both traverse through the lists, one node at a time.
# When p1 reaches the end of a list, then redirect it to the head of B.
# Similarly when p2 reaches the end of a list, redirect it the head of A.
# If at any point p1 meets p2, then its the intersection node.
# Otherwise, they don't intersect. The two pointers p1 and p2 are guaranteed to meet
# for intersected lists once both are redirected as we have equalized their traversal lengths.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        if not p1 or not p2:
            return None
        
        while p1 and p2:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next
            
        if not p1:
            p1 = headB
        if not p2:
            p2 = headA
        
        while p1 and p2:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next

        if not p1:
            p1 = headB
        if not p2:
            p2 = headA

        while p1 and p2:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
