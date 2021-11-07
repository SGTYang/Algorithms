class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans=[]
        def gp(op,cp,p):
            if op < 0 or cp < 0:
                return
            if op ==0 and cp == 0:
                ans.append(p)
                
            if op>0:
                gp(op-1,cp,p+'(')
            
            if op<cp:
                gp(op,cp-1,p+')')
        
        gp(n,n,'')
        return ans
