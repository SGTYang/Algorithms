class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        if not isConnected: return 0
        visited = set()
        
        def dfs(index):
            for i in range(len(isConnected[index])):
                if isConnected[index][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                cnt += 1
        
        return cnt
