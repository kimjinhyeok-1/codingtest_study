# 기존 방향성
def solution1(name):
    N = len(name)
    
    answer = 0
    for n in name:
        if n == 'A':
            continue
        up = ord(n) - ord('A')
        down = 26 - up
        answer += min(up, down)
    
    """""
    비트마스킹이랑 이것저것 시도해봤으니 결국 못 품
    비트마스킹으로 풀면 안 된다고 함
    n이 20이라 2^20은 너무 커서 불가능
    """""
    
    return answer

# 정답 코드
def solution(name):
    N = len(name)
    
    answer = 0
    for n in name:
        if n == 'A':
            continue
        up = ord(n) - ord('A')
        down = 26 - up
        answer += min(up, down)

    move = N - 1
    
    for i in range(N):
        # i를 지난 뒤 연속된 A 구간 끝
        next_i = i + 1
        while next_i < N and name[next_i] == 'A':
            next_i += 1
        
        # 오른쪽으로 i까지 → 왼쪽으로 회차 → 끝 구간
        move = min(move, i + i + (N - next_i))    # 정→역
        move = min(move, (N - next_i) + (N - next_i) + i)  # 역→정
    
    return answer + move