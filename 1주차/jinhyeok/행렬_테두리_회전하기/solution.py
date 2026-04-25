def solution(rows, columns, queries):
    ans = []
    arr = []
    # 초기 배열 만들기
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(i * columns + j+1)
        arr.append(temp)
    
    for x1,y1,x2,y2 in queries:
        # idx값으로 변경
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
            
        # 덮어씌워지는 것 때문에 왼쪽 위의 변수 따로 저장
        temp = arr[x1][y1]
        min_val = temp
            
        # 왼쪽변 위로 밀기
        for r in range(x1, x2):
            arr[r][y1] = arr[r+1][y1]
            min_val = min(min_val, arr[r][y1])
                
        # 아래쪽변 왼쪽으로 밀기
        for c in range(y1, y2):
            arr[x2][c] = arr[x2][c+1]
            min_val = min(min_val, arr[x2][c])
        # 오른쪽변 아래쪽으로 밀기
        for r in range(x2-1, x1-1, -1):
            arr[r+1][y2] = arr[r][y2]
            min_val = min(min_val, arr[r+1][y2])
                
        # 위쪽변 오른쪽으로 밀기
        for c in range(y2-1,y1-1,-1):
            arr[x1][c+1] = arr[x1][c]
            min_val = min(min_val, arr[x1][c+1])
            
        arr[x1][y1+1] = temp
            
        ans.append(min_val) 
        
    return ans