# N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오

# 1. input으로 입력값 받음
# 2. 리스트로 변환
# 3. 각각 정수로 변환 하면서 더하기

# 갯수를 받는 것은 의미 없음..
# n = input()

print('더할 수를 나열하여 입력해주세요')
numbers = list(input())
sum_numbers = 0

for i in numbers:
    sum_numbers += int(i)

print(sum_numbers)
