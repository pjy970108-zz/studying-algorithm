from bisect import bisect_left, bisect_right

def cnt_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) 
array = list(map(int, input().split())) 
cnt = cnt_range(array, x, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)