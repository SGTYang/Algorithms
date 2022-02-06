class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        prev = nums[0]
        for i in range(1,len(nums)):
            prev = prev ^ nums[i]
        return prev
