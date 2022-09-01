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
        walker = runner = head
        
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if walker is runner:
                return True
        return False
            