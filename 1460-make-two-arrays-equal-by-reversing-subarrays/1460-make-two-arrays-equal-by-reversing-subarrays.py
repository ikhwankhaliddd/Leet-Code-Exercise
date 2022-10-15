class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        sortedTarget = sorted(target)
        sortedArr = sorted(arr)
        if sortedTarget != sortedArr:
            return False
        return True