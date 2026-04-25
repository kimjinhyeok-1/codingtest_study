def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    ans = ''.join(stack)
    if k > 0:
        return ans[:-k]
    else:
        return ans