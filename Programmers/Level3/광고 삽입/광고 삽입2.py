def solution(play_time, adv_time, logs):
    answer = ''
    #input 타입?
    #output 타입?
    def toString(time):
        h = time//3600
        res = time-h*3600
        m = res//60
        s = res-60*m
        return(str("%02d"%h)+":"+str("%02d"%m)+":"+str("%02d"%s))
    
    def convertTime(time):
        res=time.split(":")
        return int(res[0])*3600+int(res[1])*60+int(res[2])
    
    play_arry = [0]*(convertTime(play_time)+1)
    
    for i in range(len(logs)):
        tmp=logs[i].split("-")
        play_arry[convertTime(tmp[0])] += 1
        play_arry[convertTime(tmp[1])] -= 1
    
    for i in range(1,len(play_arry)):
        play_arry[i] = play_arry[i-1]+play_arry[i]
        
    box = convertTime(adv_time)
    
    idx = 0
    playtime = sum(play_arry[:box])
    max_sum = playtime
    
    for i in range(box,len(play_arry)):
        playtime = playtime+play_arry[i]-play_arry[i-box]
        if playtime > max_sum:
            idx = i-box+1
            max_sum = playtime

    return toString(idx)
