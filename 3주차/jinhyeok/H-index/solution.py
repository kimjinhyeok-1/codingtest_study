# 1번 풀이
from bisect import bisect_left

def solution(cit):
    answer = 0
    cit.sort()
    l = len(cit)
    
    print(cit)
    for i in range(l):
        idx = l - bisect_left(cit, cit[i])
        if idx >= cit[i]:
            return cit[i]
    return answer

# 2번 풀이
def solution(cit):
    answer = 0
    cit.sort()
    l = len(cit)
    
    for i in range(l):
        # i번째 논문 인용 횟수 이상인 것들은 l - i
        h = l - i
        # 만약 i번재 논문 인용 횟수가 h 이상이면 바로 return
        if cit[i] >= h:
            return h
    return answer