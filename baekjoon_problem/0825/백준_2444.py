n = int(input())

for i in range(1, n):
    print(' '*(n-i)+'*'*(i-1)+'*'+'*'*(i-1)+' '*(n-i))
for i in range(0, n):
    print(' '*(i)+'*'*(n-i-1)+'*'+'*'*(n-i-1))