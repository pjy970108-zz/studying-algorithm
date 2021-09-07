N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]

answer = []
num = 0
for t in range(N):
    num += K-1
    if num >= len(arr): # 만약 arr의 길이보다 num이 크다면
        num = num%len(arr)
    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer[:]), ">", sep='')