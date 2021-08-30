odds = []

for i in range(7):
    x = int(input())
    if x % 2 == 1:
        odds.append(x)

if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))