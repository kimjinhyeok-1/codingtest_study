from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[-1]*m for _ in range(n)]
    
    queue = deque([(0,0)])
    visited[0][0] = 1
    
    while queue:
        cy, cx = queue.popleft()

        for d in range(4):
            ny, nx = cy+dy[d], cx+dx[d]
            if (0 <= ny < n and 0 <= nx < m) and maps[ny][nx] and visited[ny][nx] == -1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[cy][cx]+1
    
    return visited[n-1][m-1]