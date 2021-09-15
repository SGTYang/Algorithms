class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [None for _ in nums]
        
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left]**2
                left += 1
            else:
                answer[i] = nums[right]**2
                right -= 1
        return answer
