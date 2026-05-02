from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((0,begin))
    visited = {}
    if target not in words:
        return 0
    
    while q:
        cnt, word = q.popleft()
        
        if word == target:
            return cnt
        for next_word in words:
            temp = 0
            for i in range(len(next_word)):
                if word[i] != next_word[i]:
                    temp += 1
            if temp == 1 and next_word not in visited:
                visited[next_word] = True
                q.append((cnt + 1, next_word))
    return 0