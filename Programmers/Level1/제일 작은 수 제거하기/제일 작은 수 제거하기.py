def solution(arr):
  
    if len(arr) == 1:
        return [-1]
    
    arr.remove(sorted(arr, reverse=True)[-1])
    return arr
