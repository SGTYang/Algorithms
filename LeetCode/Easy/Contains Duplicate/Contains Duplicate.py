class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(set(nums))
        if length == len(nums):
            return False
        else:
            return True
