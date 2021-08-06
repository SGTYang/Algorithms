class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        s = 0
        
        while left < right:
            if height[left] > height[right]:
                s = max(s, height[right]*(right-left))
                right -= 1
            else:
                s = max(s, height[left]*(right-left))
                left += 1
        return s
