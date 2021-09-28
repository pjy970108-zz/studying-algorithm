import sys
from collections import deque
NUM_p = int(input())
for _ in range(NUM_p):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))
    answer = 0
    best = max(queue)
    while queue:
        if len(queue) == 1:
            queue.popleft()
            answer += 1
            if M == 0:
                print(answer)
        else:
            if queue[0] == best:
                queue.popleft()
                best = max(queue)
                answer += 1
                if M == 0:
                    print(answer)
                    break
                else:
                    M -=1
            else:
                queue.append(queue.popleft())
                if M == 0:
                    M = len(queue)-1
                else:
                    M -= 1






