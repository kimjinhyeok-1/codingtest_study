from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 102
    board = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    
    for left_x, left_y, right_x, right_y in rectangle:
        for x in range(left_x*2, right_x*2+1):
            for y in range(left_y*2, right_y*2+1):
                board[x][y] = 1
                
    for left_x, left_y, right_x, right_y in rectangle:
        for x in range(left_x*2+1, right_x*2):
            for y in range(left_y*2+1, right_y*2):
                board[x][y] = 0
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    sx, sy = characterX*2, characterY*2
    ex, ey = itemX*2, itemY*2
    
    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    
    while queue:
        cx, cy, cnt = queue.popleft()
        if cx == ex and cy == ey:
            return cnt//2
        
        for d in range(4):
            nx, ny = cx+dx[d], cy+dy[d]
            if not visited[nx][ny] and board[nx][ny] == 1:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True
        
    return -1