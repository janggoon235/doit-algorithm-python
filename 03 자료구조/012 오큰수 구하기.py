# 수열 A에서 i번째의 수 보다 오른쪽에 있으면서 Ai 보다 큰 수 중 가장 왼쪽에 있는 수를 구하시오
# 없을 때는 -1로 표기한다.

def get_nge(numbers: str):
    number_list = list(map(int, numbers.split()))  # 수열 전체
    numbers_len = len(number_list)  # 수열 길이
    answer = [0] * numbers_len  # 결과 list
    result = ''  # 결과 예쁘게 보이게 하는...
    stack = []  # 스택(파이썬에 따로 스택 형태는 없어 리스트로 적용하는 듯)

    for i in range(numbers_len):
        # 오큰수가 있을 경우
        while stack and number_list[stack[-1]] < number_list[i]:
            # - 두 가지를 한꺼번에 하는 부분
            # 1. stack 의 첫 요소(저장된 index)를 뺌
            # 2. answer의 해당 index에 number list[i]를 저장
            answer[stack.pop()] += number_list[i]

        # 있든 없든 순서대로 스택에 index 채우기
        stack.append(i)

    # 오큰수가 없는 index에 -1 채우기
    while stack:
        # 역시 두 가지를 한꺼번에
        # 1. stack의 첫 요소를 뺌(수열의 index)
        # 2. answer의 해당 index에 -1을 넣음
        answer[stack.pop()] = -1

    # 예쁘게 프린트 하려고 스트링 만들기
    for i in answer:
        result += f'{i} '

    # 끝에 공백 제거
    result.strip()

    return result


print(get_nge('3 5 2 7'))
print(get_nge('9 5 4 8'))
