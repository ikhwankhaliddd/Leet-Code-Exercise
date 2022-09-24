class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        poss = [0 for i in range(0, n + 1)]
        
        poss[0] = 0
        poss[1] = 1
        poss[2] = 2
        
        for i in range(3, n + 1):
            subposs = [poss[j] for j in range(i-2, i-1+1)]
            
            poss[i] = sum(subposs)
            
        return poss[n]
        