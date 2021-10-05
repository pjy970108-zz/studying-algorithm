n = int(input())
m = int(input())
matrix = [[0] * (n+1) for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
    
result = []

def dfs(start):
    visit[start] = 1
    for i in range(1, n+1):
        if matrix[start][i] == 1 and visit[i]==0:
            result.append(i)
            dfs(i)
    return len(result)
print(dfs(1))