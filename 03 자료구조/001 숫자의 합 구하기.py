# N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오

# 1. input으로 입력값 받음
# 2. 리스트로 변환
# 3. 하나씩 더하기

def get_sum(numbers: str):
    number_list = [int(num) for num in numbers]
    sum_numbers = 0

    for num in number_list:
        sum_numbers += num

    return sum_numbers


print(get_sum('54321'))
print(get_sum('70000000000000000000'))
print(get_sum('10987654321'))
