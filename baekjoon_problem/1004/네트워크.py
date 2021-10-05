def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)] # 빈리스트 만듦
    for com in range(n): # 네트워크 탐색
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer # 네트워크 탐색 후 return

def DFS(n, computers, com, visited):
    visited[com] = True # 방문
    for connect in range(n):
        if connect !=com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
