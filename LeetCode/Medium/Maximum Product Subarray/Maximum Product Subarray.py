class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_min = prev_max = answer= nums[0]
        
        for i in range(1,len(nums)):
            current_max = max(prev_min*nums[i], prev_max*nums[i], nums[i])
            
            answer = max(current_max, answer)
            
            prev_min = min(prev_min*nums[i], prev_max*nums[i], nums[i])
            prev_max = current_max
            
        return answer
