from collections import deque
def solution(cacheSize, cities):
    total_time = 0
    que = deque([])
    que_dict = {}
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    for i in range(len(cities)):
        if cities[i] in que_dict:
            total_time += 1
            que.remove(cities[i])
            que.append(cities[i]) 
        else:
            if len(que)<cacheSize:
                que.append(cities[i])
                que_dict[cities[i]] = que_dict.get(cities[i],0)+1
            elif que:
                name = que.popleft()
                del que_dict[name]
                que.append(cities[i])
                que_dict[cities[i]] = 1    
            total_time += 5  
            
    return total_time
