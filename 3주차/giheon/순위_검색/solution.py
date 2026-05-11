from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    DB = defaultdict(list)
    
    for i in info:
        infor = i.split()
        condition = infor[:-1]
        score = int(infor[-1])
        
        for r in range(5):
            for combo in combinations(range(4), r):
                temp = condition.copy()
                for idx in combo:
                    temp[idx] = "-"
                
                key = "".join(temp)
                DB[key].append(score)
                
    for key in DB:
        DB[key].sort()
                
    answer = []
    
    for q in query:
        clean_query = q.replace(" and ", " ")
        search = clean_query.split()
        
        s_condi = search[:-1]
        s_scor = int(search[-1])
        s_key = "".join(s_condi)
        
        scores = DB[s_key]
        
        idx = bisect_left(scores, s_scor)
        
        cnt = len(scores) - idx
        answer.append(cnt)
    
    return answer