from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 두배 하기 위해 102로 설정하고 grid visited 모두 설정
    answer = 0
    N = 102
    q = deque()
    grid = [[-1] * N for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x : x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    grid[x][y] = 0
                elif grid[x][y] !=0:
                    grid[x][y] = 1
    
    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    q.append((cx,cy))
    visited[cx][cy] = 0
    
    while q:
        x,y = q.popleft()
        if x == ix and y == iy:
            return visited[x][y] // 2
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0<= nx < N and 0<= ny < N and grid[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return 0