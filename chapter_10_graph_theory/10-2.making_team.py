def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

n, m = map(int, input().spilt())

parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i]=i

for i in range(m):
    oper, a, b = map(int, input().spilt())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(paren, a) == find_parent(parent, b):
            print("yes")
        else:
            print("no")