class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        counter = Counter(nums)
        ans = []

        for i in counter:
            if counter[i] == 1:
                ans.append(i)
            else:
                continue
        return ans