#ダイクストラ法
#あらかじめ幅優先探索を用いて、各町からタクシーを乗り換えずにいける道路を求めて、
#それをコストに持つ新たなグラフを作成する
import heapq
from collections import deque

N,K = map(int, input().split())

Taxi = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(N+1)]
for i in range(K):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
# print(G)
# print(Taxi)

#先にタクシーが乗り越え無しで行ける道を運賃込みで探索するためにBFS
#運賃込みのリスト
G2 = [[] for _ in range(N+1)]
Q = deque()
visited = [False] * (N+1)
for i in range(N):
    #各町からタクシーで探索できる範囲を調べる
    cost = Taxi[i][0]
    lim = Taxi[i][1]
    Q.append((i+1, lim)) #町と移動可能回数
    while len(Q) != 0:
        now, depth = Q.popleft()
        
        visited[now] = False #初期化
        if depth == 0:
            continue
        
        for v in G[now]:
            if visited[v] == False:
                Q.append((v, depth-1))
                visited[v] = True
                
                #有向隣接リストを作成(頂点番号とコスト)
                #開始した頂点から指定の本数以内でいける町
                G2[i+1].append((v, cost))
        
# for i in G2:
#     print(*i)


# 作成したG2をダイクストラ法で探索
hQ = []
INF = 10**10
#最小運賃を格納
Fare = [INF] * (N+1)
Fare[1] = 0
#始点,開始の最小運賃は0
heapq.heappush(hQ, (0, 1))

#ダイクストラで探索
while len(hQ) != 0:
    (cost, current) = heapq.heappop(hQ)
    
    if cost > Fare[current]:
        continue
    
    for v in G2[current]:
        if cost + v[1] < Fare[v[0]]:
            Fare[v[0]] = cost + v[1] #最小運賃更新
            #heapに追加
            heapq.heappush(hQ, (Fare[v[0]], v[0]))
            
print(Fare[N])