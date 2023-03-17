# 방향 없는 그래프가 주어졌을 때 연결 요소(Connected component) 의 개수를 구하는 프로그램을 작성하시오
import sys

sys.setrecursionlimit(10 ** 6)

input_data: list[list[int]] = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]
node_len: int = 6
edge_len: int = len(input_data)
a: list[list[int]] = [[] for _ in range(node_len + 1)]
visited: list[bool] = [False] * (node_len + 1)


def dfs(index: int):
    visited[index] = True
    for i in a[index]:
        if not visited[i]:
            dfs(i)


for edge in input_data:
    # 양방향 엣지라 양쪽에 에지를 더한다.
    a[edge[0]].append(edge[1])
    a[edge[1]].append(edge[0])

count = 0

for i in range(1, node_len + 1):  # 연결 노드 중 방문하지 않았던 노드만 탐색
    if not visited[i]:
        count += 1
        dfs(i)

print(count)