# 수열 A를 오름차순으로 정렬했을 때 앞에서 부터 K번째에 있는 수 구하기

a = [4, 1, 2, 3, 5]


def swap(i: int, j: int):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def partition(start: int, end: int):
    if start + 1 == end:
        if a[start] > a[end]:
            swap(start, end)
        return end

    # 중간 수를 찾아 pivot으로 삼는다
    size_range = (start + end) // 2
    swap(start, size_range)
    pivot = a[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot < a[j] and j > 0:
            j -= 1

        while pivot > a[i] and i < len(a) - 1:
            i += 1

        if i <= j:
            swap(i, j)
            i += 1
            j -= 1

    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정
    a[start] = a[j]
    a[j] = pivot

    return j


def quick_sort(start: int, end: int, k: int):
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quick_sort(start, pivot - 1, k)
        else:
            quick_sort(pivot + 1, end, k)


k = 2
quick_sort(0, len(a) - 1, k)
print(a[k - 1])
