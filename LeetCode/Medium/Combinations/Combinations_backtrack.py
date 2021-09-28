class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtracking(remain,comb,nex):
            if remain == 0:
                sol.append(comb.copy())
            else:
                for i in range(nex,n+1):
                    comb.append(i)
                    
                    backtracking(remain-1,comb,i+1)
                    
                    comb.pop()
        backtracking(k,[],1)
        return sol
