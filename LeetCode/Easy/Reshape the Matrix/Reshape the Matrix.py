class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        tmp = []
        for i in mat:
            for j in i:
                tmp.append(j)   
        if r*c != len(tmp):
            return mat
    
        index = 0
        answer = []
        
        for i in range(r):
            tmp_arry = []
            for j in range(c):
                tmp_arry.append(int(tmp[index]))
                index += 1
            answer.append(tmp_arry)
            
        return answer
