def solution(money):
    def check_max(arr):
        n = len(arr)
        DP = [0]*n
        
        DP[0] = arr[0]
        DP[1] = max(arr[0], arr[1])
        
        for i in range(2, n):
            DP[i] = max(DP[i-1], DP[i-2]+arr[i])
            
        return DP[-1]
    
    return max(check_max(money[:-1]), check_max(money[1:]))