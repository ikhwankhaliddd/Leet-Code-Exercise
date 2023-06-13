class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        arr = []
        
        
        for index in range(len(grid)):
            temp = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if j == index:
                        temp.append(grid[i][j])
            arr.append(temp)
            temp = []
            
        count = 0
        for x in range(len(grid)):
            for y in range(len(arr)):
                if grid[x] == arr[y]:
                    count += 1
        return count


