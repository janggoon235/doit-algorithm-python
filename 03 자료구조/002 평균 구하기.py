# 모든 값을 '점수/최대값*100'으로 고치고 이의 평균을 구하라

def get_avg(scores: str):
    my_list = list(map(int, scores.split(' ')))
    max_score = max(my_list)
    sum_score = sum(my_list)
    return sum_score * 100 / max_score / len(my_list)


print(get_avg('40 80 60'))
print(get_avg('10 20 30'))
print(get_avg('1 100 100 100'))
print(get_avg('1 2 4 8 16'))
print(get_avg('3 10'))
