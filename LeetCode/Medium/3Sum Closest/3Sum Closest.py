class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_val = nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                if target == s:
                    return s
                elif s < target:
                    if abs(min_val-target) > abs(s-target):
                        min_val = s
                    left += 1
                else:
                    if abs(min_val-target) > abs(s-target):
                        min_val = s
                    right -= 1
        return min_val
