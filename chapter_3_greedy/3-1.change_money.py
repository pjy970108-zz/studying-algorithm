n = 1260
count_n = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count_n += n // coin
    n %= coin

print(count_n)