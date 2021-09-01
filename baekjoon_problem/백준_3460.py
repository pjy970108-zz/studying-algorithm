n = int(input())
z = []
for _ in range(n):
    m = bin(int(input()))
    m_list=list(m[2:])
    for k, i in enumerate(m_list[::-1]):
        if int(i) == 1:
            print(int(k), end=' ')