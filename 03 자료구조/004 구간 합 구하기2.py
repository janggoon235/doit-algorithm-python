# N*N개의 수가 N*N크기의 표에 채워져 있다.
# (X1, Y1) 에서 (X2,Y2)까지의 합을 구하라
# 구하는 횟수M은 100,000회까지

# 질의 개수가 10만이므로 구간 합 배열을 사용해야 한다.

import sys

input = sys.stdin.readline

# 매번 이렇게 입력값 받아서 하는 형식은 매우 불편...
# 테스트 하기도 힘들다.

def get_sum():
    # n: 데이터 행 개수
    # m: 질의 개수
    n, m = map(int, input().split())

    a = [[0] * (n + 1)]
    d = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        a_row = [0] + [int(x) for x in input().split()]
        a.append(a_row)

    for i in range(i, n + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1] + a[i][j]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        result = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]
        print(result)


get_sum()