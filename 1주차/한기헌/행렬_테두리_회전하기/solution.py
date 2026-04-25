# 기존 방향성이 처음에는 board를 정말 굳이 그려야할까? 하는 고민에 시간 좀 녹이다가 결국엔 borad 그려서 푸는걸로 확정
# rotate하는거 구현해서 풀었음
# x,y가 각각 row와 col인데 기존에 풀던대로 x축 y축 방향으로 잘 못 이해해서 시간날림. 문제 재대로 읽을 것.

def solution1(rows, columns, queries):
    answer = []
    board = [[columns*i+j+1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        temp = board[x1][y1]
        min_val = temp
        
        for i in range(x1, x2):
            board[i][y1] = board[i+1][y1]
            min_val = min(min_val, board[i][y1])
        
        for j in range(y1, y2):
            board[x2][j] = board[x2][j+1]
            min_val = min(min_val, board[x2][j])
        
        for i in range(x2, x1, -1):
            board[i][y2] = board[i-1][y2]
            min_val = min(min_val, board[i][y2])
        
        for j in range(y2, y1, -1):
            board[x1][j] = board[x1][j-1]
            min_val = min(min_val, board[x1][j])
        
        board[x1][y1+1] = temp
        
        answer.append(min_val)
    
    return answer


# 다른 사람 풀이 구경하는데 deque로 푸는 흥미로운 풀이 있어서 가져와봄.
from collections import deque

def solution(rows, columns, queries):
    answer = []
    board = [[columns*i + j + 1 for j in range(columns)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        # 테두리 수집 (시계 방향)
        border = deque()
        for j in range(y1, y2+1):
            border.append(board[x1][j])
        for i in range(x1+1, x2+1):
            border.append(board[i][y2])
        for j in range(y2-1, y1-1, -1):
            border.append(board[x2][j])
        for i in range(x2-1, x1, -1):
            border.append(board[i][y1])
        
        # 한 칸 시계 방향 회전
        border.rotate(1)
        answer.append(min(border))
        
        # 회전된 값을 보드에 다시 쓰기
        for j in range(y1, y2+1):
            board[x1][j] = border.popleft()
        for i in range(x1+1, x2+1):
            board[i][y2] = border.popleft()
        for j in range(y2-1, y1-1, -1):
            board[x2][j] = border.popleft()
        for i in range(x2-1, x1, -1):
            board[i][y1] = border.popleft()
    
    return answer