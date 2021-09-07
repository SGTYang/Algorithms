class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums)-1
        left = 0
        while left < right:
            if nums[left] == 0:
                nums.append(nums[left])
                nums.pop(left)
                right -= 1
            else:
                left += 1   
