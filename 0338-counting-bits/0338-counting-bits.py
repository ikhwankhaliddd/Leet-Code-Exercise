class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        ans = []
        temp = []
        
        for i in range(0,n+1):
            temp.append(i)
        
        for i in temp:
            num = str(bin(i)[2:])
            result = num.count('1')
            ans.append(result)
        return ans
        