class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        counter = Counter(nums)
        
        for i in counter:
            if(counter[i]) >= 2:
               return i
            continue