class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        arry = []
        
        k = k%len(nums)
        
        for i in range(len(nums)-k,len(nums)):
            arry.append(nums[i])
        for i in range(len(nums)-k):
            arry.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = arry[i]
