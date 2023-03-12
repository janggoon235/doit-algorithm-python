# N개의 수 A1, A2, ..., An이 주어졌을 때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수를 구하시오

# 1. 합 배열 생성
# 2. 합 배열 의 모든 값을 M으로 나눠 값 업데이트
# 3. 0인 개수 세기
# 4. 나머지가 같은 합배열의 개수 세기

import sys

input = sys.stdin.readline


def get_sum_remain():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * n
    c = [0] * m
    s[0] = a[0]
    answer = 0

    for i in range(1, n):
        s[i] = s[i - 1] + a[i]  # 합 배열 저장

    for i in range(n):
        remainder = s[i] % m
        if remainder == 0:
            answer += 1
        c[remainder] += 1

    for i in range(m):
        # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
        if c[i] > 1:
            answer += (c[i] * (c[i] - 1) // 2)

    print(answer)


get_sum_remain()
