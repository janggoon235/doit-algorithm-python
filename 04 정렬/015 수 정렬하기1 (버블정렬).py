# N(1~1000)개의 수를 오름차순으로 정렬하라


def bubble_sort(numbers: str):
    number_list = list(map(int, numbers.split(' ')))
    numbers_len = len(number_list)

    for i in range(numbers_len - 1):
        for j in range(numbers_len - i - 1):
            if number_list[j] > number_list[j + 1]:
                tmp_current = number_list[j]
                number_list[j] = number_list[j + 1]
                number_list[j + 1] = tmp_current

    return number_list


print(bubble_sort('5 2 3 4 1'))
