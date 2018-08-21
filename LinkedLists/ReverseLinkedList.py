# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Question: https://leetcode.com/problems/reverse-linked-list/description/

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursive Approach
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Iterative Approach
        present = head
        prev = None
        while present:
            nexter = present.next
            present.next = prev
            prev = present
            present = nexter

        return prev