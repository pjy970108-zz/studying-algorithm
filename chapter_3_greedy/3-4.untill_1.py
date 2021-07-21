n, k = map(int, input().spilt())

count=0

while n >= k:
    while n % k !=0:
        n -= 1
        count += 1
    n //= k
    count += 1
while n > 1:
    n -= 1
    count += 1
print(count)


# 다른 방법

n, k = map(int, input().split())

count = 0

while True:
    target = (n//k)*n
    count += n-target
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += n-1
print(count)
