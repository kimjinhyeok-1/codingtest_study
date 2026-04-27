# 모든 경우의 수를 다 보고 타깃에 맞는 갯수 구하는거니까 완전탐색
def solution(numbers, target):
    n = len(numbers)
    def dfs(numbers, target, cnt, val):
        if cnt == n:
            if val == target:
                return 1
            else:
                return 0
        else:
            answer = 0
            answer += dfs(numbers, target, cnt+1, val+numbers[cnt])
            answer += dfs(numbers, target, cnt+1, val-numbers[cnt])
        return answer
    
    answer = dfs(numbers, target, 0, 0)
    return answer