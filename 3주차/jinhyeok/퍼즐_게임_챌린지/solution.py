# 현재 퍼즐 난이도: diff
# 현재 퍼즐 소요시간: time_curr
# 이전 퍼즐의 소요시간: time_prev
# 숙련도: level

# 1번 풀이
def solution(diffs, times, limit):
    answer = 0
    for level in range(1, max(diffs) + 1):
        if diffs[0] > level:
            answer = (diffs[0] - level) * times[0] + times[0]
        else:
            answer = times[0]
        for i in range(1, len(times)):
            if diffs[i] > level:
                answer += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
            else:
                answer += times[i]
        if answer <= limit:
            return level
    return answer

# 2번 풀이
# 현재 퍼즐 난이도: diff
# 현재 퍼즐 소요시간: time_curr
# 이전 퍼즐의 소요시간: time_prev
# 숙련도: level

def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)
    while left <= right:
        level = (left + right) // 2
        
        total = 0
        if diffs[0] > level:
            total = (diffs[0] - level) * times[0] + times[0]
        else:
            total = times[0]
        for i in range(1, len(times)):
            if diffs[i] > level:
                total += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
            else:
                total += times[i]
        if total <= limit:
            answer = level
            right = level - 1
        else:
            left = level + 1
    return answer