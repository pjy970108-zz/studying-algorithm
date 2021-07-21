n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

big_one=num_list[-1]
second_one = num_list[-2]

result=0

while True:
    for i in range(k):
        if m == 0:
            break
        result += big_one
        m -= 1
    if m == 0:
        break
    result += second_one

    m -= 1
print(result)


## another version
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

big_one=num_list[-1]
second_one=num_list[-2]

#큰수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1) # 나머지만큼 큰수가 들어감

result = 0
result += count*big_one
result += (m-count)*second_one # 두번째로 큰수 더하기
print(result)