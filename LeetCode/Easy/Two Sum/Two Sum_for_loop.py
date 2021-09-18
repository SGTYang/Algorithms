class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}
        for i in range(len(nums)):
            find = target-nums[i]
            
            if find in check:
                return [i, check[find]]
            else:
                check[nums[i]] = i
