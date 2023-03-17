import sys

sys.setrecursionlimit(10 * 6)
node_len = 8
arrive = False
edges = [[1, 7], [3, 7], [4, 7], [3, 7], [4, 7], [3, 4], [4, 6], [3, 5], [0, 4], [2, 7]]
edge_len = len(edges)
a = [[] for _ in range(edge_len + 1)]
visited = [False] * (edge_len + 1)


def dfs(cur_node, depth):
    global arrive
    if depth == 5:  # 깊이가 5가 되면 종료
        arrive = True
        return

    visited[cur_node] = True

    for i in a[cur_node]:
        if not visited[i]:
            dfs(i, depth + 1)  # 재귀 호출마다 깊이 증가

    visited[cur_node] = False


for edge in edges:
    a[edge[0]].append(edge[1])
    a[edge[1]].append(edge[0])

for i in range(edge_len):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print('리니어하게 연결된 친구관계가 있음')
else:
    print('리니어 연결식의 친구관계가 없음')
