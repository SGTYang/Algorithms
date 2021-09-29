class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        result = []
        subset = []
        
        def backtracking(result, visited, subset, nums):
            if len(subset) == len(nums):
                result.append(subset)
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtracking(result, visited, subset+[nums[i]], nums)
                    visited.remove(i)
        
        backtracking(result, visited, subset, nums)
        return result
