def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total_time = 0
        
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total_time += times[i]
            else:
                mistakes = diffs[i] - mid
                total_time += mistakes * (times[i] + times[i-1]) + times[i]
                

        if total_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer