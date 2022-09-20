# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        
        def tempNode(head):
            ans.append(head.val)
            if head.next:
                head = head.next
                tempNode(head)
            return
        tempNode(head)
        if ans == ans[::-1]:
            return True
        return False