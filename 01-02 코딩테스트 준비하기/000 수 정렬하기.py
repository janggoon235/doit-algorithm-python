### N개의 수가 주어졌을 때 이를 오름차순 정렬하는 프로그램으로 작성하라
## 제한시간 2초
import datetime
import time


# 연산 횟수 = N

def test1(n):
    cnt = 1

    for i in range(n):
        print(f'연산 횟수: {str(cnt)}')
        cnt += 1


# 연산 횟수 = 3N
def test2(n):
    cnt = 1
    for i in range(n):
        print(f'연산 횟수: {str(cnt)}')
        cnt += 1
    for i in range(n):
        print(f'연산 횟수: {str(cnt)}')
        cnt += 1
    for i in range(n):
        print(f'연산 횟수: {str(cnt)}')
        cnt += 1


def count_time():
    test1_start_time = time.time()
    test1(100000)
    test1_end_time = time.time()

    test2_start_time = time.time()
    test2(100000)
    test2_end_time = time.time()

    print(f'test1 시작, 완료 시간: {test1_start_time}, {test1_end_time}')
    print(f'test1 시작, 완료 시간: {test2_start_time}, {test2_end_time}')

    print(f'test1 소요 시간: {test1_end_time - test1_start_time}')
    print(f'test2 소요 시간: {test2_end_time - test2_start_time}')


# count_time()
# test1 시작, 완료 시간: 1678601504.217794, 1678601504.7017946
# test1 시작, 완료 시간: 1678601504.7017946, 1678601504.7017946
# test1 소요 시간: 0.48400068283081055
# test2 소요 시간: 1.3789985179901123

# test1, test2의 연산 횟수는 3배차이가 난다.
# 코딩테스트에서는 일반적으로 상수를 무시하므로 시간복잡도는 O(n)으로 동일하다.

# 연산 횟수 = N의 2제곱
def test3(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print(f'연산 횟수: {str(cnt)}')
            cnt += 1


def print_test3_process_time():
    test3_start_time = time.time()
    test3(100000)
    test3_end_time = time.time()

    print(f'시작, 완료 시간: {test3_start_time}, {test3_end_time}')
    print(f'소요 시간: {test3_end_time - test3_start_time}')


# 음청 오래 걸림 100000 * 100000
# print_test3_process_time()
