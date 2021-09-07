import sys
from collections import deque


def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    if len(dq)==0:
        return -1
    else: 
        return dq.popleft()

def pop_back():
    if len(dq)==0:
        return -1
    else: 
        return dq.pop()

def size():
    return len(dq)

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0

def front():
    if len(dq) == 0:
        return -1
    else:
        return dq[0]
def back():
    if len(dq) == 0:
        return -1
    else:
        return dq[-1]



N = int(sys.stdin.readline())

dq = deque([])

for _ in range(N):
    command = sys.stdin.readline().split()
    order = command[0]
    if order == 'pop_front':
        print(pop_front())
    elif order == 'pop_back':
        print(pop_back())
    elif order == 'push_front':
        push_front(int(command[1]))
    elif order == 'push_back':
        push_back(int(command[1]))
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())





 
