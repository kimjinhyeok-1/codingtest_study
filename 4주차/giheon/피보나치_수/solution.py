def solution(n):
    DP = [0]*(n+1)
    DP[1] = 1
    
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]
        
    answer = DP[n]%1234567
    return answer