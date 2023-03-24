import collections


def bfs(cur_r, cur_c):
    q = collections.deque()
    q.append([cur_r, cur_c, 0, 1])
    V[0][cur_r][cur_c] = 1
    while q:
        cur_r, cur_c, brk_cnt, depth = q.popleft()
        if cur_r == N - 1 and cur_c == M - 1:
            return depth
        for dx, dy in dr:
            nxt_r, nxt_c = cur_r + dx, cur_c + dy
            if 0 <= nxt_r <= N - 1 and 0 <= nxt_c <= M - 1:
                if A[nxt_r][nxt_c] == 1 and brk_cnt < K and not V[brk_cnt + 1][nxt_r][nxt_c]:
                    q.append([nxt_r, nxt_c, brk_cnt + 1, depth + 1])
                    V[brk_cnt + 1][nxt_r][nxt_c] = 1
                elif A[nxt_r][nxt_c] == 0 and not V[brk_cnt][nxt_r][nxt_c]:
                    q.append([nxt_r, nxt_c, brk_cnt, depth + 1])
                    V[brk_cnt][nxt_r][nxt_c] = 1
    return -1


N, M, K = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
V = [[[0] * M for _ in range(N)] for k in range(K + 1)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
print(bfs(0, 0))