# N개의 수를 오름차순 정렬하라
# 병합 정렬


def merge_sort(start: int, end: int):
    if end - start < 1:
        return

    middle = int(start + (end - start) / 2)
    merge_sort(start, middle)
    merge_sort(middle + 1, end)
    k = start
    index1 = start
    index2 = middle + 1

    for i in range(start, end + 1):
        tmp[i] = number_list[i]

    while index1 <= middle and index2 <= end:  # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            number_list[k] = tmp[index2]
            k += 1
            index2 += 1

        else:
            number_list[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= middle:  # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        number_list[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= end:  # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        number_list[k] = tmp[index2]
        k += 1
        index2 += 1


number_list = [5, 4, 3, 2, 1, 3, 73, 7, 8, 95]
numbers_len = len(number_list)
tmp = [0] * (numbers_len + 1)

number_list.insert(0, 0)
merge_sort(1, numbers_len)

number_list.pop(0)
print(number_list)
