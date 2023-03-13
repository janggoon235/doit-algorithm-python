# 1. 최소값 가능성 없는 데이터 삭제
# 2. window 크기 밖 데이터 삭제
from collections import deque


def get_minimums(min_range: int, target_data: str):
    data_list = list(map(int, target_data.split(' ')))
    my_deque = deque()
    result = []

    for i in range(len(data_list)):
        while my_deque and my_deque[-1][0] > data_list[i]:
            my_deque.pop()

        my_deque.append((data_list[i], i))
        if my_deque[0][1] <= i - min_range:
            my_deque.popleft()

        result.append(my_deque[0][0])

    return result


print(get_minimums(3, '1 5 2 3 6 2 3 7 3 5 2 6'))
