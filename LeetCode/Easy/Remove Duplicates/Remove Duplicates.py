class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
        return index
