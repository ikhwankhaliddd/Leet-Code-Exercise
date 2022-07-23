class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        temp = []
        for i in range(len(b)):
            int_to_str = str(b[i])
            temp.append(int_to_str)
            concat = "".join(temp)
            concat = int(concat)
        
        return pow(a,concat, mod = 1337)
        