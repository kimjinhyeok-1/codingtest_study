# 기존 풀던 방향성 -> 다익스트라로 어떻게 해보려다가 실패. 예외 케이스 생각 못 하고 그냥 비용 적은것부터 연결하려다가 실패.

from collections import defaultdict
import heapq

def solution1(n, costs):
    graph_set = set()
    
    heap = []
    for cost in costs:
        a, b, c = cost
        heapq.heappush(heap, (c, a, b))
    
    answer = 0
    while len(graph_set) < n:
        c, a, b = heapq.heappop(heap)
        if not(a in graph_set and b in graph_set):
            graph_set.add(a)
            graph_set.add(b)
            answer += c
    
    return answer



# 정답 코드
# 프림 알고리즘? 이라는게 있다고 하길래 제미나이한테 받아와봤음.
# 크루스칼(Kruskal)이랑 Union-Find 이용한 풀이는 진혁이가 이미 봤길래 새로운거 가져와봄.
import heapq
from collections import defaultdict

def solution(n, costs):
    answer = 0
    
    # 1. 각 섬에서 갈 수 있는 도착지와 비용을 기록할 그래프 만들기
    graph = defaultdict(list)
    for u, v, cost in costs:
        graph[u].append((cost, v))
        graph[v].append((cost, u))
        
    # 2. 방문 여부를 체크할 set (질문자님이 쓰신 graph_set과 같은 역할!)
    visited = set()
    visited.add(0) # 0번 섬부터 탐색 시작
    
    # 3. 0번 섬과 연결된 모든 다리를 힙에 넣기
    heap = graph[0]
    heapq.heapify(heap) # 리스트를 힙 구조로 변환
    
    # 4. 모든 섬이 방문될 때까지 반복
    while len(visited) < n:
        # 현재 연결할 수 있는 다리 중 가장 비용이 적은 다리 꺼내기
        cost, node = heapq.heappop(heap)
        
        # 아직 방문하지 않은 섬이라면 연결!
        if node not in visited:
            visited.add(node)
            answer += cost
            
            # 새로 도착한 섬에서 뻗어나갈 수 있는 다리들을 힙에 추가
            for next_cost, next_node in graph[node]:
                if next_node not in visited:
                    heapq.heappush(heap, (next_cost, next_node))
                    
    return answer