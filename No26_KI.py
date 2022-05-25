import sys
sys.setrecursionlimit(int(1E+7))
#再帰関数バージョン#####################
def dfs(v,p): #現在ノード,親ノード
    if p != -1:
        val[v] += val[p]
    for ii in G[v]:
        if ii == p:
            continue #親ノードは追加しない    
        dfs(ii,v)

N,Q = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
for i in range(N-1):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for i in range(N-1):
	G[A[i]].append(B[i])
	G[B[i]].append(A[i])

val = [0] * (N+1)
for i in range(Q):
    p,x = map(int, input().split())
    val[p] += x

dfs(1, -1)

print(*val[1:])