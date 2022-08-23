class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = []
        
        while num > 0:
            if num % 2 ==  0:
                temp.append(num)
                num /= 2
            elif num % 2 == 1 :
                temp.append(num)
                num -= 1
        return len(temp)
                
        