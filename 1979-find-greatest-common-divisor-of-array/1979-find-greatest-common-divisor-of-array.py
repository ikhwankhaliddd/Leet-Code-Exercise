class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        i = max(nums)
        j = min(nums)
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a %b)
        return gcd(i,j)