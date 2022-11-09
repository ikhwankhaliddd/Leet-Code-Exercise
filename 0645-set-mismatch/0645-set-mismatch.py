class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        counter = Counter(nums)
        
        ans = [0,0]
        n = len(nums)
        
        for result in range(1,n+1):
            if counter[result] == 2:
                ans[0] = result
            if counter[result] == 0:
                ans[1] = result
        return ans
        