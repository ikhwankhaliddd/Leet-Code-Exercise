# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        index = 0
        curr = head
        
        while (curr != None):
            arr.append(curr.val)
            curr = curr.next
        
        res = sorted(list(set(arr)))
        
        def listToLinkedList(lst):
            curr = dummy = ListNode(0)
            for i in lst:
                curr.next = ListNode(i)
                curr = curr.next
            return dummy.next
        
        ans = listToLinkedList(res)
        return ans
        