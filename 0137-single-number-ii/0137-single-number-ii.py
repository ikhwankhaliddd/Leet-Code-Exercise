class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        counter = Counter(nums) # set

        for i in counter:
            if counter[i] == 1:
                return i
            continue