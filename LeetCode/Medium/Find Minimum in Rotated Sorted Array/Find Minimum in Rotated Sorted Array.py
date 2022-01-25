class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        
        while left < right:
            index = (left+right)//2
            print(left, right, index)
            if nums[index] >= nums[left] and nums[index] >= nums[right]:
                left = index+1
            else:
                right = index
        
        return nums[left]
        
