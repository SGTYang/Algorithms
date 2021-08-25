class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arry = []
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x:x[1])

        left, right = 0, len(nums)-1
        
        while left < right:

            curr_sum = nums[left][1]+nums[right][1]
            
            if curr_sum < target or (left>0 and nums[left][1]==nums[left-1][1]):
                left += 1
                
            elif curr_sum > target or (right<len(nums)-1 and nums[right][1]==nums[right+1][1]):
                right -= 1
                
            else:
                arry.extend([nums[left][0], nums[right][0]])
                left += 1
                right -= 1
        
        return arry
