class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")
        maxProfit = 0
        
        for i in prices:
            minPrice = min(minPrice,i)
            maxProfit = max(maxProfit, i-minPrice)
            
        return maxProfit
        