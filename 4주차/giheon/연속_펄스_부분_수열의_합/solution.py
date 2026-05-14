def solution(sequence):
    n = len(sequence)
    DP_1 = [(-1)**i for i in range(n+1)]
    DP_2 = [(-1)**j for j in range(1, n+2)]
    
    for i in range(1, n+1):
        DP_1[i] *= sequence[i-1]
        DP_2[i] *= sequence[i-1]
    
    for i in range(2, n+1):
        DP_1[i] = max(DP_1[i], DP_1[i-1] + DP_1[i])
        DP_2[i] = max(DP_2[i], DP_2[i-1] + DP_2[i])
    
    answer = max(max(DP_1[1:]), max(DP_2[1:]))
    return answer


# 누적합으로 푸는 방법도 있어서 공유 차원에서 가져와봄.
def solution2(sequence):
    prefix_sum = [0] # 아무것도 선택하지 않았을 때의 합인 0을 포함
    current_sum = 0
    pulse = 1
    
    for num in sequence:
        current_sum += num * pulse
        prefix_sum.append(current_sum)
        pulse *= -1
        
    # 누적합의 최댓값과 최솟값의 차이가 곧 가능한 가장 큰 연속 부분 수열의 합
    return max(prefix_sum) - min(prefix_sum)