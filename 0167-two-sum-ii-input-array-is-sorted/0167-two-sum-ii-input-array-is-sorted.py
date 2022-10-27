class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initiate ponters value and length of the array:
        n = len(numbers)
        L = 0
        R = n -1
        
        while(L < R):
            res = numbers[L] + numbers[R]
            
            if res == target:
                return [L+1, R+1]
            elif res < target:
                L += 1
            elif res > target:
                R -= 1
            else:
                return [-1,-1]
        