class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        answer = []
        
        def backtrack(permu,index,visited):
            if index ==0:
                answer.append(permu.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    permu.append(nums[i])
                    visited.add(i)
                    backtrack(permu,index-1,visited)
                    visited.remove(i)
                    permu.pop()
        
        backtrack([],len(nums),visited)
        return answer
