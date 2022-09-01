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
        walker = head
        
        while(walker):
            if walker.val is None:
                return True
            walker.val = None
            walker = walker.next
        return False