# 수 N개가 주어졌을 때 i번째 수에서 j번째 수 까지의 합을 구하는 프로그램

# 입력:
#   1. 대상 데이터
#   2. 이하 합을 구해야 하는 구간 i, j 리스트


def get_sums(main_data_str: str, range_list: list):
    result = []  # 결과 리스트
    sum_list = [0]  # 합 배열
    main_data = list(map(int, main_data_str.split(' ')))
    temp = 0

    # 합 배열 만들기
    for i in range(0, len(main_data)):
        temp = temp + int(main_data[i])
        sum_list.append(temp)

    for items in range_list:
        result.append(sum_list[items[1]] - sum_list[items[0] - 1])

    return result


final_result = get_sums('5 4 3 2 1', [[1, 3], [2, 4], [5, 5]])

print(final_result)
