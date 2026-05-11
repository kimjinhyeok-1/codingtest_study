from collections import defaultdict
def solution(clothes):
    wear = defaultdict(list)
    wear_type = set()
    for cloth in clothes:
        name, type_ = cloth
        wear[type_].append(name)
        wear_type.add(type_)
    
    answer = 1
    
    for wt in wear_type:
        answer *= len(wear[wt])+1
    
    return answer-1