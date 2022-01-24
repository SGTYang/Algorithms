class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        
        while left <= right:
            index = (left+right)//2
            
            if nums[index] == target:
                return index
            
            if nums[index] >= nums[left]:
                if nums[left]<=target<=nums[index]:
                    right = index-1
                else:
                    left = index +1
            else:
                if nums[index]<=target<=nums[right]:
                    left = index+1
                else:
                    right = index -1
                    
        return -1
