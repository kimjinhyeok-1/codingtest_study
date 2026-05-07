# 모든 경우의 수를 다 보고 타깃에 맞는 갯수 구하는거니까 완전탐색
def solution(numbers, target):
    n = len(numbers)
    def dfs(cnt, val):
        if cnt == n:
            if val == target:
                return 1
            else:
                return 0
        else:
            answer = 0
            answer += dfs(cnt+1, val+numbers[cnt])
            answer += dfs(cnt+1, val-numbers[cnt])
        return answer
    
    answer = dfs(0, 0)
    return answer