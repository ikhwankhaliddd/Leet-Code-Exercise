class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([1])
            for j in range(1,i):
                ans[i].append(ans[i-1][j-1] + ans[i-1][j])
            ans[i].append(1)
        return ans
        