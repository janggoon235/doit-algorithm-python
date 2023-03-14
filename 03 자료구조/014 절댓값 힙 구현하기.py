# 우선순위 큐 문제

# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조다.
# 1. 배열에 정수x(x != 0)을 넣는다.
# 2. 배열에서 절댓값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거한다.
#   절대값이 가장 작은 값이 여러 개일 경우에는 그중 가장 작은 수를 출력하고 << 음수출력, 그 값을 배열에서 제거한다.


# 0이 입력되면 배열에서 가장 작은 수를 출력하고, 제거한다.
# 빈 배열일 경우 0을 출력한다.
from queue import PriorityQueue


def get_smallest_number(numbers: str):
    number_list = list(map(int, numbers.split(' ')))
    my_pri_queue = PriorityQueue()
    result = ''
    for num in number_list:
        if num == 0:
            if my_pri_queue.empty():
                result += '0 '
            else:
                tmp = my_pri_queue.get()
                result += f'{tmp[1]} '
        else:
            # abs는 절대값
            my_pri_queue.put((abs(num), num))

    result.strip()
    return result


print(get_smallest_number('1 -1 0 0 0 1 1 -1 -1 2 -2 0 0 0 0 0 0 0'))
