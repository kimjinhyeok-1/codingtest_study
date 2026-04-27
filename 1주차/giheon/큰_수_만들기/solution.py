# 기존 방향성
# 일단 n이 100만이라 무조건 for문 1번으로 끝내야 한다고 생각했음.
# 그거에 갇혀서 약간 멘붕? 그리고 그리디 문제라는 생각에 스택을 활용할 생각을 못 함.
# 특히 내가 미처 생각 못 한 부분은 나는 계속 숫자 비교할 생각만 했지 내가 현재까지 뺀 숫자의 갯수를 활용해볼 생각을 못 함.

# 정답 코드
def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)