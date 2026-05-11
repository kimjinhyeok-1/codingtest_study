from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    left = 0
    dic = defaultdict(int)
    total_kind = len(set(gems))
    
    for right in range(len(gems)):
        dic[gems[right]] += 1
        while len(dic) == total_kind:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            dic[gems[left]] -= 1
            
            if dic[gems[left]] == 0:
                del dic[gems[left]]
    
            left += 1    
    return [answer[0] + 1, answer[1] + 1]