from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append((0, begin))
    visited = set()
    while queue:
        c, word = queue.popleft()
        if word == target:
            return c
            
        for w in words:
            cnt = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                if w not in visited:
                    queue.append((c+1, w))
                    visited.add(w)
    return 0