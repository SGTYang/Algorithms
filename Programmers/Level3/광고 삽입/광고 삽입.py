from datetime import datetime

def solution(play_time, adv_time, logs):
    answer = ''
    
    def toSec(time):
        time_list = time.split(':')
        return int(time_list[0])*3600+int(time_list[1])*60+int(time_list[2])
    
    def toHour(time):
        hours = time//3600
        minutes = (time%3600)//60
        sec = (time%3600)%60
        return "%02d:%02d:%02d" %(hours,minutes,sec)

    #광고 시간 초로 변환
    adv_time = toSec(adv_time)
    
    #플레이 시간 초로 변환 및 시간 만큼 배열 만들기
    play_time = toSec(play_time)
    play_arr = [0]*(play_time+1)
    
    #로그 시간 초로 변환
    for i in range(len(logs)):
        tmp = logs[i].split('-')
        play_arr[toSec(tmp[0])] += 1
        play_arr[toSec(tmp[1])] -= 1
    
    # 각 플레이 시간 합
    for i in range(1,len(play_arr)):
        play_arr[i] = play_arr[i] + play_arr[i-1]
    
    # 구하기
    max_index = 0
    playtime = sum(play_arr[:adv_time])
    max_sum = playtime
    for i in range(adv_time,len(play_arr)):
        playtime = playtime + play_arr[i] - play_arr[i-adv_time]
        if playtime > max_sum:
            max_index = i-adv_time+1
            max_sum = playtime
    
    return toHour(max_index)
