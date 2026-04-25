from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    total = s1 + s2
    cnt = 0
    
    if total % 2 !=0: return -1
    
    target = total // 2
    
    max_len = 4 * len(q1)
    
    while cnt < max_len:
        if s1 == target:
            return cnt
        elif s1 < target:
            num = q2.popleft()
            s1 += num
            q1.append(num)
        else:
            num = q1.popleft()
            s1 -= num
            q2.append(num)
        cnt += 1
    
    return -1