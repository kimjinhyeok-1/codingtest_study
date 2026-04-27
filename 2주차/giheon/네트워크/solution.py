def solution(n, computers):
    visited = [False]*n
    
    def dfs(computers, node):
        visited[node] = True
        for i, connect in enumerate(computers[node]):
            if i == node:
                continue
            if connect == 1: 
                if visited[i]:
                    continue
                else:
                    dfs(computers,i)
        return
    
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        else:
            cnt += 1
            dfs(computers, i)
    
    return cnt