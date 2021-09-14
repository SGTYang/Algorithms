from itertools import permutations
def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    
    for oper in permutations(operators, 3):

        a = oper[0]
        b = oper[1]
        tmp_list = []
        print(oper)
        for i in expression.split(a):
            print(i)
            print(i.split(b))
            tmp = [f"({j})" for j in i.split(b)]
            print(tmp)
            tmp_list.append(f"({b.join(tmp)})")
        answer.append(abs(eval(a.join(tmp_list))))
    return max(answer)
