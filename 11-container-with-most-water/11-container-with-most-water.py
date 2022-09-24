class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        lebarMax = n-1
        luas_daerah = 0
        for lebar in range (lebarMax,0,-1):
            if height[l] < height[r]:
                luas_daerah = max(luas_daerah,lebar * height[l])
                l +=1
            else:
                luas_daerah = max(luas_daerah, lebar * height[r])
                r -= 1
        return luas_daerah
        