# 기존 내 풀이
def solution1(citations):
    h = max(citations)
    answer = 0
    
    while answer == 0 and h > 0:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            answer = h
        else:
            h -= 1
    
    return answer

def solution(citations):
    # 1. 내림차순 정렬
    citations.sort(reverse=True)
    
    # 2. 인용 횟수와 논문 개수를 비교
    for i, c in enumerate(citations):
        # i + 1은 현재 논문을 포함하여 자신보다 많이 인용된 논문의 개수
        if c <= i + 1:
            return i+1
            
    # 모든 논문의 인용 횟수가 논문 개수보다 많은 경우
    return len(citations)