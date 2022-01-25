class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right-1:
            index = (left+right)//2

            if nums[index-1] < nums[index] and nums[index+1] < nums[index]:
                return index
            
            elif nums[index-1]>nums[index]:
                right = index - 1
            else:
                left = index + 1
        
        if nums[left]>=nums[right]:
            return left
        else:
            return right
