# 원래 풀던 방향성
# 간과한 사실
# 1. 수거하거나 배달해야 하는 택배가 0인 집이 끝자락에 있는 경우를 간과함.
# 2. 한 집을 두번 방문해야 하는 경우를 간과함.
def solution1(cap, n, deliveries, pickups):
    total = sum(deliveries)
    total2 = sum(pickups)
    cnt = (total+cap-1)//cap
    cnt2 = (total2+cap-1)//cap
    
    go = 0
    back = 0
    visited = [[] for _ in range(cnt)]
    visited2 = [[] for _ in range(cnt2)]
    i = n-1
    c = 0
    
    while i >= 0:
        if go + deliveries[i] <= cap:
            go += deliveries[i]
            visited[c].append(i+1)
            deliveries[i] = 0
            i -= 1
        else:
            deliveries[i] = go + deliveries[i] - cap
            go = 0
            c += 1
    
    i = n-1
    c = 0
    while i >= 0:
        if back + pickups[i] <= cap:
            back += pickups[i]
            visited2[c].append(i+1)
            pickups[i] = 0
            i -= 1
        else:
            pickups[i] = back + pickups[i] - cap
            back = 0
            c += 1
            
    total_trips = max(cnt, cnt2)
    answer = 0
    for k in range(total_trips):
        d_far = max(visited[k]) if k < cnt and visited[k] else 0
        p_far = max(visited2[k]) if k < cnt2 and visited2[k] else 0
        answer += max(d_far, p_far)
        
    return 2*answer

# 내 아이디어를 살려서 재대로 짠 코드
def solution1_2(cap, n, deliveries, pickups):
    total = sum(deliveries)
    total2 = sum(pickups)
    cnt = (total+cap-1)//cap if total > 0 else 0
    cnt2 = (total2+cap-1)//cap if total2 > 0 else 0
    
    visited = [[] for _ in range(cnt)]
    visited2 = [[] for _ in range(cnt2)]
    
    go = 0
    i = n-1
    c = 0
    while i >= 0:
        # 빈 집 건너뛰기
        while i >= 0 and deliveries[i] == 0:
            i -= 1
        if i < 0:
            break
        
        if go + deliveries[i] <= cap:
            go += deliveries[i]
            visited[c].append(i+1)
            deliveries[i] = 0
            i -= 1
        else:
            visited[c].append(i+1)        # ← 추가! 이번 왕복에도 이 집 방문
            deliveries[i] -= (cap - go)
            go = 0
            c += 1
    
    back = 0
    i = n-1
    c = 0
    while i >= 0:
        while i >= 0 and pickups[i] == 0:
            i -= 1
        if i < 0:
            break
        
        if back + pickups[i] <= cap:
            back += pickups[i]
            visited2[c].append(i+1)
            pickups[i] = 0
            i -= 1
        else:
            visited2[c].append(i+1)       # ← 추가!
            pickups[i] -= (cap - back)
            back = 0
            c += 1
            
    total_trips = max(cnt, cnt2)
    answer = 0
    for k in range(total_trips):
        d_far = max(visited[k]) if k < cnt and visited[k] else 0
        p_far = max(visited2[k]) if k < cnt2 and visited2[k] else 0
        answer += max(d_far, p_far)
        
    return 2*answer


# 정답 코드
def solution(cap, n, deliveries, pickups):
    answer = 0
    # 뒤에서부터 (먼 집부터) 처리
    i = n - 1
    j = n - 1
    
    while i >= 0 or j >= 0:
        # 배달할 게 없는 끝자락 건너뛰기
        while i >= 0 and deliveries[i] == 0:
            i -= 1
        # 수거할 게 없는 끝자락 건너뛰기
        while j >= 0 and pickups[j] == 0:
            j -= 1
        
        if i < 0 and j < 0:
            break
        
        # 이번 왕복에서 가야 할 가장 먼 거리
        farthest = max(i, j) + 1
        answer += farthest * 2
        
        # 배달 cap만큼 소진
        load = cap
        while i >= 0 and load > 0:
            if deliveries[i] <= load:
                load -= deliveries[i]
                deliveries[i] = 0
                i -= 1
            else:
                deliveries[i] -= load
                load = 0
        
        # 수거 cap만큼 채우기
        load = cap
        while j >= 0 and load > 0:
            if pickups[j] <= load:
                load -= pickups[j]
                pickups[j] = 0
                j -= 1
            else:
                pickups[j] -= load
                load = 0
    
    return answer