from collections import defaultdict

def solution(clothes):
    ans = 1
    dic = defaultdict(int)
    for name, kind in clothes:
        dic[kind] += 1
    
    for v in dic.values():
        ans *= (v+1)
    
    return ans - 1