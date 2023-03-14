# 1부터 N까지의 수열이 있음
# 1. 0번째 수는 버림
# 2. 1번째 수를 가장 뒤로 이동
# 1, 2를 반복하고 마지막에 남는 수를 출력
from collections import deque


def get_last_of_circle(numbers: str):
    # +1 안하면 0,1,2,3,4 된다...
    number_list = [number + 1 for number in range(int(numbers))]
    # for문 안돌려도 캐스팅 됨
    my_deque = deque(number_list)

    while len(my_deque) > 1:
        my_deque.popleft()
        my_deque.append(my_deque.popleft())

    return my_deque[0]


print(get_last_of_circle('6'))
