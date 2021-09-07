import sys
from collections import deque


def push(x):
    dq.append(x)

def pop():
    if len(dq)==0:
        return -1
    else: 
        return dq.popleft()

def size():
    return len(dq)

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0


def top():
    if len(dq) == 0:
        return -1
    else:
        return dq[-1]

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



N = int(sys.stdin.readline().rstrip())

dq = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    order = command[0]
    if order == 'push':
        push(int(command[1]))
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'top':
        print(top())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())