class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fac(num):
            if num in [0,1]:
                return 1
            return num * fac(num-1)
        ans = fac(n)
        ans_to_str = str(ans)
        ans_to_str = list(ans_to_str)
        res = 0
        for i in reversed(ans_to_str):
            if i == '0':
                res += 1
            else:
                break
        return res
        