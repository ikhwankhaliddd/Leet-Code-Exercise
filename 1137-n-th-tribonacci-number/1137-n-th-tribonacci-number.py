class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribonacci_list = [0,1,1]
        if n < 2:
            return tribonacci_list[n]
        else:
            for ans in range(n-2):
                tribonacci_list.append(sum(tribonacci_list))
                tribonacci_list.pop(0)
            return tribonacci_list.pop()