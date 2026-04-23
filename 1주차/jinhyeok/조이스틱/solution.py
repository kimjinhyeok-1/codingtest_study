def solution(name):
    change_cost = 0
    for k in name:
        change_cost += min((ord(k) - ord('A')), (ord('Z')-ord(k)+1))
    
    # n은 name의 길이로 초기화
    n = len(name)
    
    # 움직이는데 최대 비용은 n-1 이 후에 min으로 업데이트
    move_cost = n - 1
    
    # 0번째부터 n-1번째까지 모두 확인
    for i in range(n):
        next_i = i + 1
        # 현재 위치에서 다음 A 뭉텅이가 언제 나오는지 체크
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        #next_i 인덱스 값은 A 뭉텅이 바로 뒤에 위치
        
        # move_cost와 뒤로 갔다가 오는 값, 앞으로 갔다가 오는 값 min값 비교
        move_cost = min(move_cost, (2*i + n-next_i),(i+2*(n-next_i)))
        
    return change_cost + move_cost