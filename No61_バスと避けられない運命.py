#ワ―シャルフロイド法で解ける
N,M = map(int, input().split())

#隣接リスト作成
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,t = map(int, input().split())
    G[a-1].append((b-1,t))
    G[b-1].append((a-1,t))

INF = 10**10
d = [[INF]*(N) for _ in range(N)]
#初期化
for i in range(N):
    d[i][i] = 0
    for j in G[i]:
        d[i][j[0]] = j[1]
        
#ワ―シャルフロイド法
for k in range(N): #中継地点
    for i in range(N): #始点
        if d[i][k] == INF:
            continue
        for j in range(N): #終点
            if d[k][j] == INF:
                continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = INF
for i in range(N):
    mx = max(d[i])
    if ans > mx:
        ans = mx

print(ans)