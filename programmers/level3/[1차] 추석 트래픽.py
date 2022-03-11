def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond

def get_start_time(time, duration_time):
    t = duration_time[:-1]
    t = int(float(t) * 1000)
    return get_time(time) - t + 1
    
def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for log in lines:
        time = log.split()
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer
solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
# solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"])
# solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])
# solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])