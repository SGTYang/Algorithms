class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        answer = []
        def combination(i,arry):
            if i == len(digits):
                if len(arry) > 0:
                    answer.append(''.join(arry))
                return
            
            for j in letter_dic[digits[i]]:
                arry.append(j)
                combination(i+1, arry)
                arry.pop()
            
        combination(0, [])
            
        return answer
