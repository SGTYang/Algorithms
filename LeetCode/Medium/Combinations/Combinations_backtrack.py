class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        answer = []
        def backtrack(combi,index,start):
            if index==0:
                # Shallow Copy 사용(리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 됨) 
                answer.append(combi.copy())
                return
            
            for i in range(start,n+1):
                combi.append(i)
                backtrack(combi,index-1,i+1)
                combi.pop()
        
        backtrack([],k,1)
        return answer
                
            
