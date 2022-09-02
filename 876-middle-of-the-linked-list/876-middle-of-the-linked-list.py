# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        turto = head
        hare = head
        
        while hare != None and hare.next != None:
            turto = turto.next
            hare = hare.next.next
        return turto
        