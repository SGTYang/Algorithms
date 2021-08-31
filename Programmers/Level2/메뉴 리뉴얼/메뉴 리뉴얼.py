from collections import Counter
from itertools import permutations, combinations
def solution(orders, course):
    
    answer = []
    for i in course:
        arry_tmp = []
        for j in range(len(orders)):
            list_tmp = list(orders[j])
            list_tmp.sort()
            orders[j] = "".join(list_tmp)        
            tmp = ["".join(i) for i in list(combinations(orders[j],i))]
            arry_tmp.extend(tmp)
        count = Counter(arry_tmp)
        max_count = 0
        for i in count:
            max_count = max(count.get(i),max_count)
        answer.extend([key for key, value in count.items() if max_count >1 and value == max_count])
        
    answer.sort()
    return answer
