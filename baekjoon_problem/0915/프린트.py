from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque([(v, i) for i , v in enumerate(priorities)]) # location과 값 저장
    waiting_list = []
    
    while len(dq):
        tmp = dq.popleft()
        if dq and max(dq)[0] > tmp[0]: # 최대값이 0번째 값보다 크면
            dq.append(tmp)
        else: #최대값이 같거나 작으면
            answer += 1 #answer에 1을 더하고
            if tmp[1] == location: # 만약 tmp의 위치 값이 location과 같으면
                break
            
        
    return answer
