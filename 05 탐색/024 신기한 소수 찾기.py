import sys

sys.setrecursionlimit(10 * 6)

basic_primes = [2, 3, 5, 7]
result = []


# 소수 구하기 함수
def get_is_prime(num: int):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


# dfs
def dfs(digits: int, num: int):
    if len(str(num)) == digits:
        result.append(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:  # 짝수면 탐색 불필요
                continue
            elif get_is_prime(num * 10 + i):  # 소수이면 자릿수 늘림
                dfs(digits, num * 10 + i)


def print_special_primes(digits: int):
    for p in basic_primes:
        dfs(digits, p)
    print(result)


print_special_primes(6)
