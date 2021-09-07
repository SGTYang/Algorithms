class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return nums
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            if nums[left]%2!=0 and nums[right]%2==0:
                tmp = nums[right] 
                nums[right] = nums[left]
                nums[left] = tmp
                left += 1
                right -= 1
                
            elif nums[left]%2 ==0:
                left += 1
                
            elif nums[right]%2 !=0:
                right -= 1
        
        return nums
