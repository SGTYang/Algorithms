from collections import deque 
def solution(p):
    
    def is_balanced(p):
        if len(p)!=0 and p.count('(') == p.count(')'):
            return True
        else:
            return False
    
    def is_perfect(p):
        stack = deque()
        for i in range(len(p)):
            if p[i] == '(':
                stack.append(')')
            elif p[i] == ')' and len(stack)>0:
                if p[i] != stack.popleft():
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
        
    def process(p):
        u = v = ''
        index = 0
        while not is_balanced(u):
            u += p[index]
            index += 1
        v = p[index:]
        return (u,v)
    
    def whole(p):
        if len(p)==0:
            return p
        else:
            u,v = process(p)
            if is_perfect(u):
                return u+whole(v)
            else:
                tmp = '(' + whole(v) +')'
                u = list(u)
                u = u[1:-1]
                for i in range(len(u)):
                    if u[i] == '(':
                        u[i] = ')'
                    elif u[i] == ')':
                        u[i] = '('
                return tmp + ''.join(u)

    return whole(p)
