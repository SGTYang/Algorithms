def solution(n, arr1, arr2):
    answer = []
    new_arr = []
    for i in range(len(arr1)):
        tmp = list((format(arr1[i]|arr2[i],'b')).zfill(n))
        ans = ""
        for j in tmp:
            if j == '1':
                ans += "#"
            else:
                ans += " "
        answer.append(ans)
    
    return answer
