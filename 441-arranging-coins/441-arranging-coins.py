class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
        
            temp = mid * (mid + 1) // 2
            
            if temp == n:
                return mid
            elif temp < n :
                low = mid + 1
            else:
                high = mid - 1
        return high
        