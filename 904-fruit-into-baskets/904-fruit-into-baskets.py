from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        hashMap = defaultdict(int)
        
        start = 0
        end = 0
        maxFruits = 0
        
        for i in range(len(fruits)):
            hashMap[fruits[i]] += 1
            while len(hashMap) > 2:
                hashMap[fruits[start]] -= 1
                if hashMap[fruits[start]] == 0:
                    del hashMap[fruits[start]]
                start += 1
            maxFruits = max(maxFruits, i - start+1)
        return maxFruits
            
        