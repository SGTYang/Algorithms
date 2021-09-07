class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=sorted(nums, key = lambda x:abs(x))
        return [i*i for i in nums]
