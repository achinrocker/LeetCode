# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        next_node = dummy_head
        while (l1!= None and l2!= None):
            if l1.val <= l2.val:
                next_node.next = l1
                l1 = l1.next
            else:
                next_node.next = l2
                l2 = l2.next
            next_node = next_node.next

        if (l1 != None):
            while(l1 != None):
                next_node.next = l1
                l1 = l1.next
                next_node = next_node.next

        if (l2 != None):
            while(l2 != None):
                next_node.next = l2
                l2 = l2.next
                next_node = next_node.next

        return dummy_head.next
