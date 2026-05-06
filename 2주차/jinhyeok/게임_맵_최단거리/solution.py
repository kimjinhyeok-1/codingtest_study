
from collections import deque
def solution(maps):
    q = deque([(0,0)])
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    r = len(maps)
    c = len(maps[0])
    dist = [[-1] * c for _ in range(r)]
    dist[0][0] = 1
    
    es = False
    while q:
        gr, gc = q.popleft()
        for dr, dc in d:
            nr, nc = gr + dr, gc + dc
            if nr == r-1 and nc == c-1:
                answer = dist[gr][gc] + 1
                return answer
            if 0<=nr<r and 0<=nc<c:
                if maps[nr][nc] == 1 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[gr][gc] + 1
                    q.append((nr,nc))
    
    answer = -1
    return answer
    

