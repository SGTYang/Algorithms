class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(target):
            left, right = 0, len(nums)
            
            while left < right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        mini= search(target)
        maxi = search(target+1)-1
        
        if mini <= maxi:
            return [mini, maxi]
        
        return [-1,-1]
