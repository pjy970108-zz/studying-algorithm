locate = input()
row = int(locate[1])
col = int(ord(locate[0])-int(ord("a")))+1

step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result=0
for k in step:
    next_row = row + k[0]
    next_col = col + k[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)