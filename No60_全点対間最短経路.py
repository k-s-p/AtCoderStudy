#ワ―シャルフロイド法の練習問題
V,E = map(int, input().split())
G = [[] for _ in range(V)]

for i in range(E):
    s,t,d = map(int, input().split())
    G[s].append((t,d))
    
# print(G)

#ワ―シャルフロイド法で求める
INF = 10**10
d = [[INF]*V for _ in range(V)]
#初期化
for i in range(V):
    d[i][i] = 0
for i in range(V):
    for j in G[i]:
        d[i][j[0]] = j[1]

for k in range(V): #kを中継する
    for i in range(V): #始点
        if d[i][k] == INF:
            continue
        for j in range(V): #終点
            if d[k][j] == INF:
                continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

#負の閉路があるか判定
ok = True
for i in range(V):
    if d[i][i] < 0:
        ok = False
        break

if ok:
    for i in range(V):
        for j in range(V):
            if d[i][j] == INF:
                d[i][j] = 'INF'
        print(*d[i])
else:
    print('NEGATIVE CYCLE')