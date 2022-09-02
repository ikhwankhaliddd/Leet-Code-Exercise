# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
                
        turt = rabb = head
        
        while rabb is not None and rabb.next is not None:
            turt = turt.next
            rabb = rabb.next.next
        return turt
        