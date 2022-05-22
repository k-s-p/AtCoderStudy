#bit全探索
#問題サイズがそんなに大きくない
import itertools

N,M = map(int, input().split())

#隣接リストの作成
G = [list() for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

#bit全探索
ans = 0
for bit in range(1 << N):
    A = [] #派閥の組み合わせ
    for i in range(N):
        if bit & (1 << i):
            A.append(i+1)
    #派閥がなりたつかどうか(２つの組み合わせで知り合いかどうか判定)
    ok = True
    for i in itertools.combinations(A, 2):
        if i[0] not in G[i[1]]:
            ok = False
            break
    if ok:
        ans = max(ans, len(A))

print(ans)
