n, m = map(int, input().split())
result = 0

for i in range(n):
    list_n=list(map(int, input().split()))
    min_value=min(list_n)
    result=max(result, min_value)
print(result)