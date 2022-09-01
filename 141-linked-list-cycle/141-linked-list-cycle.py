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
        # lst = []
        # while head is not None:
        #     if head in lst:
        #         return True
        #     lst.append(head)
        #     head = head.next
        # return False
        
        try:
            walker = head
            runner = head.next

            while walker is not runner:
                walker = walker.next
                runner = runner.next.next
            return True
    
        except:
            return False