import random

findNumber = random.randrange(1, 101)
# print(f'findNumber: {findNumber}')

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break

# 시간복잡도
# 빅-오메가: 1번
# 빅-세타: N/2
# 빅-오: N

# 코테에서는 빅-오 기준으로 수행시간을 계산
# 최악을 염두에 두어야 함.
