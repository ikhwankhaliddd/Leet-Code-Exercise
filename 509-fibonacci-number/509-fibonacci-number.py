class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibb(num):
            if num in [0,1]:
                return num
            return fibb(num-1) + fibb(num-2)
        ans = fibb(n)
        return ans
        