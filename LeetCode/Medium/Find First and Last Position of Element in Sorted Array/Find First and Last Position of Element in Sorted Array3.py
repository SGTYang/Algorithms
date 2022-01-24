class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            index = (left+right)//2
            if nums[index] == target:
                left=right=index
                while left>=0 and nums[left] == target:
                    left -= 1
                while right<len(nums) and nums[right] == target:
                    right +=1
                return [left+1,right-1]
                
            elif nums[index] > target:
                right = index-1
            else:
                left = index+1

        return [-1,-1]
