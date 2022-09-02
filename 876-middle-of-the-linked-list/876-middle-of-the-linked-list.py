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
        rabb = head
        
        while rabb != None and rabb.next != None:
            turto = turto.next
            rabb = rabb.next.next
        return turto
        