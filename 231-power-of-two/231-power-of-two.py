class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def pows(n):
            if n % 2 == 0 and n > 0:
                return pows(n//2)
            else:
                return n == 1
        return pows(n)
            