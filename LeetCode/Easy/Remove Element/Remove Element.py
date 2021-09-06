class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = [v for i,v in enumerate(nums) if val!=v]
        del nums[:]
        nums.extend(tmp)
