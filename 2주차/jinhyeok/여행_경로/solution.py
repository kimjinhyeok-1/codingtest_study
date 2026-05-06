# 1번 풀이
def solution(tickets):
    graph = {}
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort()
        
    answer = ['ICN']
    
    def dfs(cur):
        # answer이랑 tickets + 1 이랑 같으면 모두 다 쓴거니깐 다시 되돌리기
        if len(answer) == len(tickets) + 1:
            return True
        # 경로 계속 들어오다가 갈 곳 없으면 False 리턴
        if cur not in graph:
            return False
        # cur랑 연결되어 있는거 모두 조회
        for i in range(len(graph[cur])):
            nxt = graph[cur][i]
            # 다음 경로가 사용되지 않았으면 사용으로 바꾸고 answer에 추가
            if nxt != 'USED':
                graph[cur][i] = 'USED'
                answer.append(nxt)
                if dfs(nxt):
                    return True
                # 경로가 아니였다면 제거하고 다음 경로 확인해야됨 pop하고 USED 취소
                answer.pop()
                graph[cur][i] = nxt
    dfs('ICN')
    return answer

#2번 풀이
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in tickets:
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort(reverse=True)
    
    path = []
    
    def dfs(cur):
        while graph[cur]:
            dfs(graph[cur].pop())
        path.append(cur)
    
    dfs("ICN")
    
    return path[::-1]