import itertools


def solution(nums):
    combination = list(itertools.combinations(nums, 3))
    count=0
    for i in combination:
        sum_list=[] # i가 바뀔떄마다 초기화 시켜야함
        for k in range(sum(i)): # i의 합을 하나씩 나눠봄
            if sum(i) % (k+1) == 0: # 나머지가 0이면 listk에 더함
                sum_list.append(k)
        if len(sum_list) == 2:
            count += 1

        
    return count