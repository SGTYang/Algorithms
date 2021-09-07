class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_num = 0
        cnt = 0
        
        if len(set(nums)) < 3:
            return max(nums)
        
        nums = list(set(nums))
        nums.remove(max(nums))
        nums.remove(max(nums))
        
        return max(nums)
