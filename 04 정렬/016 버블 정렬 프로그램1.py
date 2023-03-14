# c++로 작성된 버블정렬 코드 해석하고 같은 기능의 함수 만들기
# 책 98p

def get_none_sorted_count(numbers: str):
    number_list = [(num, index) for index, num in enumerate(list(map(int, numbers.split(' '))))]
    numbers_len = len(number_list)
    sorted_list = sorted(number_list)
    max_num = 0

    for i in range(numbers_len):
        if max_num < sorted_list[i][1] - i:
            max_num = sorted_list[i][1] - i

    return max_num + 1


print(get_none_sorted_count('10 1 5 2 3'))
