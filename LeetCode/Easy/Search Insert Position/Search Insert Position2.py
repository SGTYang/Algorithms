class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            index = (left+right)//2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index-1
            else:
                left = index+1
    
        return left
        
