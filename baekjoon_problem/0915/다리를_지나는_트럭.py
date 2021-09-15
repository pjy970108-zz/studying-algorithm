def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    answer = 0
    sum_bridge=0
    while bridge:
        tmp = bridge.pop(0)
        sum_bridge -= tmp
        if len(truck_weights) != 0 and sum_bridge + truck_weights[0] <= weight:
            tmp = truck_weights.pop(0)
            bridge.append(tmp)
            sum_bridge += tmp
        else:
            bridge.append(0)
        if len(truck_weights) == 0 and sum_bridge==0:
            break
        answer += 1
    return answer+1