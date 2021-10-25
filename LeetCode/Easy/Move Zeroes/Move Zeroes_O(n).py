class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = []
        
        index = 0
        for i in range(len(nums)):
            if nums[i] !=0 :
                arr.append(nums[i])
        
        arr += (len(nums)-len(arr))*[0]
        
        for i in range(len(nums)):
            nums[i] = arr[i]
