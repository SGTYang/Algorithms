class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        while left<=right:
            index = left+(right-left)//2
            
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left+=1
            else:
                right-=1
        
        if nums[index]<target:
            return index+1
        else:
            return index
