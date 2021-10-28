def solution(arr):
    answer = 0
    
    first = arr[0]
    if len(arr) ==1:
        return first
    
    def uclid(a,b):
        if a<b:
            a,b = b,a
        
        while a%b !=0:
            tmp = a%b
            a,b = b, tmp
        
        return b
    
    for i in range(1,len(arr)):
        u = uclid(first,arr[i])
        first = (first/u)*(arr[i]/u)*u
        
    return first
