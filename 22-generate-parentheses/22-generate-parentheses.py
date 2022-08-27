class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def dfs(arr, s, right, left):
            if right == 0 and left == 0 :
                arr.append(s)
                return
            
            if left > 0:
                dfs(arr, s+"(", right, left-1)
                
            if left < right and right > 0:
                dfs(arr, s+")", right-1, left)
                
            return arr
        
        ans = dfs([],'',n,n)
        
        return ans
            
        