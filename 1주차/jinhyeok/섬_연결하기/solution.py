'''
    처음보는 MST -> 크루스칼 유니온-파인드로 풀기
'''
def solution(n, costs):
    answer = 0
    
    # 1. 대장이 누구인지 확인
    def find(parents, x):
        if parents[x] != x:
            parents[x] = find(parents, parents[x])
        return parents[x]
    
    # 2. 대장이 같다면 합치기
    def union(parents, a, b):
        rootA = find(parents, a)
        rootB = find(parents, b)
        if rootA < rootB: 
            parents[rootB] = rootA
        else:
            parents[rootA] = rootB
            
    # 3. kruskal 알고리즘
    costs.sort(key= lambda x: x[2]) # 비용 순으로 정렬
    parents = [i for i in range(n)] # 각자 n의 부모는 처음에는 n
    
    for a,b,cost in costs:
        if find(parents,a) != find(parents,b):
            union(parents, a, b)
            answer += cost
    return answer