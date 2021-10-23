class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2

            if nums[left] == target and nums[right] == target:
                return [left, right]
            elif nums[mid] < target and left+1 != right:
                left = mid + 1
            elif nums[mid] > target and left+1 != right:
                right = mid - 1
            else:
                if nums[left] != target: left += 1
                if nums[right] != target: right -= 1

        return [-1,-1]
