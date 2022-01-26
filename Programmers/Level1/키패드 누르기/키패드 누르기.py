def solution(numbers, hand):
    answer = ''
    cordinate = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    L_current = (3,0)
    R_current = (3,2)
    
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            L_current = cordinate[numbers[i]]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            R_current = cordinate[numbers[i]]
        else:
            Cy, Cx = cordinate[numbers[i]]
            Ly, Lx = L_current 
            L_dis = abs(Ly-Cy)+abs(Lx-Cx)
            Ry, Rx = R_current
            R_dis = abs(Ry-Cy)+abs(Rx-Cx)
            
            if L_dis == R_dis:
                if hand == 'right':
                    R_current = cordinate[numbers[i]]
                    answer += 'R'
                else:
                    L_current = cordinate[numbers[i]]
                    answer += 'L'
            elif L_dis > R_dis:
                R_current = cordinate[numbers[i]]
                answer += 'R'
            else:
                L_current = cordinate[numbers[i]]
                answer += 'L'
            
    return answer
