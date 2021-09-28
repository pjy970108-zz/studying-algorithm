from collections import deque
def solution(prices):
    answer = []
    que=deque(prices)
    while que:
        count = 0
        tmp = que.popleft()
        for i in que:
            count += 1
            if tmp > i:
                break
        answer.append(count)    
    
    
    return answer