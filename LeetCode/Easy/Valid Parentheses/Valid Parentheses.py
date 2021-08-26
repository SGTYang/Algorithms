class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = ["(","[","{"]
        close_parentheses = [")","]","}"]
        
        stack = []
        
        for i in s:
            if i in open_parentheses:
                stack.append(close_parentheses[open_parentheses.index(i)])
            else:
                if len(stack) != 0 and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
