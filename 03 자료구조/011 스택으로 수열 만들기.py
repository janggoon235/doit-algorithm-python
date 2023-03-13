def get_stack_cals(numbers: str):
    print('start')

    number_list = list(map(int, numbers.split(' ')))
    stack = []
    num = 1
    answer = []

    print(f'length of numbers: {len(number_list)}')

    for i in number_list:
        su = i
        if su >= num:  # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
            while su >= num:
                stack.append(num)
                num += 1
                answer.append(f'+{su}')
            stack.pop()
            answer.append(f'-{su}')
        else:  # 현재 수열값 < 오름차순 자연수:pop()을 수행해 수열 원소를 꺼냄
            n = stack.pop()
            # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
            if n > su:
                answer = 'No'
                break
            else:
                answer.append(f'-{su}')

    return answer


print(get_stack_cals('4 3 6 8 7 5 2 1'))
print(get_stack_cals('1 2 5 3 4'))
