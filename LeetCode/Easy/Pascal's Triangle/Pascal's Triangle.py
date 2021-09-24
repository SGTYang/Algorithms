class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = []
        
        for i in range(1,numRows+1):
            tmp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    tmp.append(1)
                else:
                    tmp.append(answer[i-2][j-1]+answer[i-2][j])
            answer.append(tmp)
        
        return answer
