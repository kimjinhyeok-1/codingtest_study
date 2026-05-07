from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    # key 값 넣을 딕셔너리 하나 만들어놓기
    dic = defaultdict(list)
    
    # info에 들어있는거 하나당 16가지 종류 만들어 놓기
    # java backend junior pizza 면 각각 하나씩 -도 들어갈 수 있으니깐 2^4
    # 만든거 key값으로 만들어서 value 값은 score로 dic에 넣기 
    for i in info:
        # 각각 split하고 score랑 분리
        temp = i.split()
        x = temp[:-1]
        score = int(temp[-1])
        # 0,1,2,3 은 인덱스 값 0~4까지 돌리면서 몇개 선택할건지 정하고 그 안에 -대신 넣기
        for n in range(5):
            for com in combinations([0,1,2,3], n):
                copi = x[:]
                for idx in com:
                    copi[idx] = '-'
                
                key = "".join(copi)
                dic[key].append(score)
    
    # 각 key 별로 list 오름차순으로 정렬하기 bisect_left 쓰기 위해서
    for key in dic: dic[key].sort()
    
    # query에서 하나씩 가져오면서 만족하는게 몇개인지 확인 (bisect_left 이용)
    
    ans = []
    for q in query:
        # and replace 해주고 split해서 다시 q에 저장
        temp = q.replace("and ", "").split()
        key = "".join(temp[:-1])
        target = int(temp[-1])
        
        # bisect_left 이용해서 target 값이 위치할수 있는 곳 찾기
        # value list 값이 [1,2,4,5] 이고 target 값이 3 이면 idx는 2
        # value 길이인 4에서 idx, 2빼주면 2가나오고 그말은 4,5가 들어갈 수 있다는 의미
        
        arr = dic[key]
        idx = bisect_left(arr, target)
        ans.append(len(arr) - idx)
        
    return ans