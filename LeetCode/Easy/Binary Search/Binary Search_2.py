class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right, left = 0, len(nums)-1
        
        while right <= left:
            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                right = mid+1
            elif nums[mid] > target:
                left = mid-1
        return -1
