class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        L = 0
        R = n -1
        
        while (L < R):
            res = numbers[L] + numbers[R]
            
            if res == target:
                return [L+1, R+1]
            elif res < target:
                L += 1
            elif res > target:
                R -= 1
            else:
                return [-1,-1]