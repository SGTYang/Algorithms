import math
def solution(fees, records):
    answer = []
    
    def toMin(time):
        times=time.split(":")
        return (int(times[0])*60+int(times[1]))
    
    car = []
    in_time = {}
    used_time = {}
    car = []
    
    for i in range(len(records)):
        tmp = records[i]
        records[i] = tmp.split(" ")
        car.append(records[i][1])
    
    car = list(set(car))

    for i in range(len(records)):
        if records[i][2] == 'IN':
            in_time[records[i][1]] = toMin(records[i][0])
                
        elif records[i][2] == 'OUT':
            used_time[records[i][1]] = used_time.get(records[i][1],0)+toMin(records[i][0])-in_time[records[i][1]]
            del in_time[records[i][1]]
    for i in car:
        if i in in_time:
            used_time[i] = used_time.get(i,0)+1439-in_time[i]
            
    car = sorted(car)

    for i in car:
        if used_time[i] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((used_time[i]-fees[0])/fees[2])*fees[3])
        
    return answer
