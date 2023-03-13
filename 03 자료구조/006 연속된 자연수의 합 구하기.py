# 자연수 N(1<= N <= 10000000)이 연속된 자연수의 합으로 나타나는 경우의 수 구하기

def get_cases_count(n: int):
    cnt = 1
    start_i = 1
    end_i = 1
    sum_case = 1

    while end_i != n:
        # 2. 합이 목표 수가 되었을 때 경우의 수(cnt)를 추가하고, start index, end index 를 하나씩 옮긴다.
        if sum_case == n:
            cnt += 1
            end_i += 1
            sum_case += end_i

        # 3. 합이 목표 수보다 크면 start index를 하나씩 늘려간다. (합은 당연히 start가 달라지니 start index를 빼준다.)
        elif sum_case > n:
            sum_case -= start_i
            start_i += 1

        # 1. 전체 합(sum)이 목표 수가 될 때까지 end index를 하나씩 더한다.
        else:
            end_i += 1
            sum_case += end_i

    return cnt


print(get_cases_count(int(input())))
