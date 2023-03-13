# N(1~15,000)개의 고유의 수 중 2개의 수(1~100,000)를 합쳐 M(1~10,000,000)이 되는 경우의 수

# 1. 고유의 수 들을 정렬한다.
# 2. 투 포인터 이동으로 두 값의 합이 M일때 카운트를 하고, 두 포인터 모두 이동
# 3. 두 포인터가 만날 때 종료

def get_equal_cases_cnt(m: int, material_data: str):
    material_list = list(map(int, material_data.split(' ')))
    material_list.sort()
    i = 0  # first point
    j = len(material_list) - 1  # second point
    cnt = 0

    while i < j:
        if material_list[i] + material_list[j] < m:
            i += 1
        elif material_list[i] + material_list[j] == m:
            i += 1
            j -= 1
            cnt += 1
        else:
            j -= 1

    return cnt


# print(get_equal_cases_cnt(int(input()), input()))
print(get_equal_cases_cnt(9, '2 7 4 1 5 3'))
