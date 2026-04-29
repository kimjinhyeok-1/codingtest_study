from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for A, B in sorted(tickets, reverse=True):
        graph[A].append(B)
    
    answer = []
    
    def dfs(con):
        while graph[con]:
            nc = graph[con].pop()
            dfs(nc)
        answer.append(con)
    
    dfs("ICN")
    
    return answer[::-1]