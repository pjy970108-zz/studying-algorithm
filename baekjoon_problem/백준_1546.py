n = int(input())
m = list(map(int, input().split()))
correct_num=[]

for i in m:
    correct_num.append(i/max(m)*100)
print(sum(correct_num)/n)