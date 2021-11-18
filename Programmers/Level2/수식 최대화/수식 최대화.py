from itertools import permutations
def solution(expression):
    oper = ['+','-','*']
    stack = []
    for i in permutations(oper):
        a = i[0]
        b = i[1]
        tmp=expression.split(a)
        for j in range(len(tmp)):
            tmp[j] = tmp[j].split(b)
            for k in range(len(tmp[j])):
                tmp[j][k] = str(eval(tmp[j][k]))
            tmp[j] = str(eval(b.join(tmp[j])))
        stack.append(abs(eval(a.join(tmp))))

    return max(stack)
