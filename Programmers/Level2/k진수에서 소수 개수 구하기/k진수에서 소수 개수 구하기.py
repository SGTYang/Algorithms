import math
def solution(n, k):
    answer = 0
    
    def is_prime_number(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False 
        return True 
    
    def convert_notation(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)
        return convert_notation(q, base) + T[r] if q else T[r]    
    
    c = convert_notation(n,k)
    index = 0
    pointer = 0
    tmp = ''
    arr = []
    
    while pointer < len(c):
        if c[pointer] != '0':
            tmp += c[pointer]
        elif c[pointer] == '0':
            index=pointer
            arr.append(tmp)
            tmp = ''
        pointer +=1
    arr.append(tmp)
    
    for i in range(len(arr)):
        if arr[i] != '' and is_prime_number(int(arr[i])):
            answer += 1 
    
    return answer
