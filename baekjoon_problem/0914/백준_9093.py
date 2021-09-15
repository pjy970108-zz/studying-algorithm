N = int(input())
for _ in range(N):
    sen = list(input().split())
    k=[]
    for i in sen:
        k.append(i[::-1])
    print(' '.join(k))