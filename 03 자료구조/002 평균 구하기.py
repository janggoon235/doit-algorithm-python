# 모든 값을 '점수/최대값*100'으로 고치고 이의 평균을 구하라

def get_avg(scores: str):
    my_list = list(map(int, scores.split(' ')))
    max_score = max(my_list)
    sum_score = sum(my_list)
    return sum_score * 100 / max_score // len(my_list)


print('점수를 스페이스로 구분하여 입력해주세요')
print(get_avg(input()))
