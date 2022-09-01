# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slower = faster = head
        
        while(faster and faster.next):
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False