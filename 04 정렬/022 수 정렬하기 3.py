# N개의 수 오름차수 정렬
# 계수 정렬

def counting_sort_asc(numbers: str):
    number_list = list(map(int, numbers.split()))
    result = ''
    count = [0] * 10001

    for num in number_list:
        count[num] += 1

    for i in range(10001):
        if count[i] != 0:
            for _ in range(count[i]):
                result += f'{i} '

    result.strip()
    return result


print(counting_sort_asc('215 15 344 8 372 294 100 8 145 24 198 831'))
