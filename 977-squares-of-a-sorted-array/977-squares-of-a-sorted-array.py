class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for i in nums:
            squared_num = i ** 2
            ans.append(squared_num)
        return sorted(ans)
        