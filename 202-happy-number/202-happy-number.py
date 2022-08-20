class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 7 :
            return True
        if len(str(n)) < 2 :
            return False
        happyNumber = sum(int(s) ** 2 for s in str(n))
        return self.isHappy(happyNumber)