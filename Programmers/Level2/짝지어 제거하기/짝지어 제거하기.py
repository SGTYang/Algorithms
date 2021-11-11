def solution(s): 
    arry = []    
    for i in s:
        
        if len(arry) == 0: 
            arry.append(i)
        elif arry[-1] == i: 
            arry.pop()
        else: 
            arry.append(i)
            
    if len(arry) == 0: 
        return 1
    else: 
        return 0
