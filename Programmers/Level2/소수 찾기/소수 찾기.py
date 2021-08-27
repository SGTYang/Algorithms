from itertools import permutations, combinations
import math
def solution(numbers):
    answer = 0
    permu = []
    for i in range(1,len(numbers)+1):
        tmp = list(permutations(numbers, i))
        [permu.append(int(k)) for k in ["".join(j) for j in tmp]]
    permu = set(permu)
    for i in permu:
        if check_prime(i):
            answer +=1
    return answer

def check_prime(n):
    if n == 0 or n ==1:
        return False
    if n == 2 or n ==3 :
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True
        
