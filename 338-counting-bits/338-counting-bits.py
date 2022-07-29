class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        
        for i in range(n + 1):
            sub_str = str(bin(i)[2:])
            counter = sub_str.count('1')
            ans.append(counter)
        return ans
        