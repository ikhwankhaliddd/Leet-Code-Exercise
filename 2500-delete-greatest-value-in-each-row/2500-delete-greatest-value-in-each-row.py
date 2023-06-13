class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        
        for i in range(n):
            grid[i].sort()
            
        grid = list(zip(*grid))
        
        
        return sum(max(x) for x in grid)
        