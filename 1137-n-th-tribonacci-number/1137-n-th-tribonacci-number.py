class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0,1,1]
        if n < 2:
            return arr[n]
        else:
            for ans in range(n-2):
                arr.append(sum(arr))
                arr.pop(0)
            return arr.pop()