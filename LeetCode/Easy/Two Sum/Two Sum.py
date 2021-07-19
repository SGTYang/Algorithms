class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i,number in enumerate(nums):
            rest = target - number
            if rest in check:
                return [i, check[rest]]
            else:
                check[number] = i
