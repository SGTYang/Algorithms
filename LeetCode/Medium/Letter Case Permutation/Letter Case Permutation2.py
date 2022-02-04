class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        
        def backtrack(arry,index,start):
            if index == 0:
                answer.append("".join(arry.copy()))
                
            for i in range(start,len(s)):

                if s[i].isalpha():
                    lar = s[i].upper()
                    low = s[i].lower()
                    arry.append(lar)
                    backtrack(arry,index-1,i+1)
                    arry.pop()
                    arry.append(low)
                    backtrack(arry,index-1,i+1)
                    arry.pop()
                else:
                    arry.append(s[i])
                    backtrack(arry,index-1,i+1)
                    arry.pop()
                
        backtrack([],len(s),0)
        return answer
