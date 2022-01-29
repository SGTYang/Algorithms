class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        pointer = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[pointer],nums[i] = nums[i],nums[pointer]
                pointer +=1
