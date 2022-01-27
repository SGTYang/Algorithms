import heapq
def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key=lambda x: x[0])
    heap = []
    prev = -1
    i=current_time=total_time = 0
    while i < len(jobs):
        for j in range(len(jobs)):
            if current_time >= jobs[j][0] > prev:
                heapq.heappush(heap, [jobs[j][1],jobs[j][0]])
        
        if len(heap)>0:
            request_time, run_time = heapq.heappop(heap)
            prev = current_time
            current_time += request_time
            total_time += current_time - run_time
            i+=1
        else:
            current_time +=1
    
    return total_time//len(jobs)
