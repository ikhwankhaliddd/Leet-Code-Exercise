class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        while num != 0 :
            if num % 2 :
                num -= 1
            else:
                num /= 2
            count += 1
        return count
                
        