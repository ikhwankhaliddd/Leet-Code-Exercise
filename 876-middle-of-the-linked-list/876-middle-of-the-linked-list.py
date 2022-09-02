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
        
        turt = rabb = head
        
        while rabb is not None and rabb.next is not None:
            turt = turt.next
            rabb = rabb.next.next
        return turt
        