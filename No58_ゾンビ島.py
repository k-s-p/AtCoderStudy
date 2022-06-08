# まず、島のマップを隣接リストで作成する
# 次に、ゾンビに支配された町全てと１本の道で繋がる架空の町から、
# S+1本の道でいける危険な街を見つける(BFS)
# 危険な街のコストと安全な街のコストを宿代で設定する
# その後、最小コストのルートをダイクストラ法で探索

from collections import deque
import heapq

N,M,K,S = map(int, input().split())
P,Q = map(int, input().split())

#　危険な町かゾンビがいる町かどうか
# 0安全、1危険、2ゾンビ
Denger = [0] * (N+1)
for i in range(K):
    c = int(input())
    Denger[c] = 2

G = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
# 危険な街を探索する
# 町0はゾンビの町に１本道でいけると仮定
for i in range(1, N+1):
    if Denger[i] == 2:
        G[0].append(i)
#町0からS+1本以内でいける町を探索
T = deque()
T.append(0)
depth = [0] * (N+1)
while len(T) != 0:
    pos = T.popleft()
    if depth[pos] == S+1:
        break
    
    for i in G[pos]:
        if depth[i] == 0:
            T.append(i)
            depth[i] = depth[pos] + 1
            if Denger[i] == 0:
                Denger[i] = 1

#ゾンビの町と危険な町がわかったので、町1からゴールまでの最小コストの経路をダイクストラ法で探索
hQ = []
INF = 10**10
#最省コストを格納
distance = [INF] * (N+1)
distance[1] = 0
#始点,開始のコストは0
heapq.heappush(hQ, (0, 1))
#ダイクストラ法で探索
while len(hQ) != 0:
    (cost, current_node) = heapq.heappop(hQ)

    #もし取り出した距離が記録されている最短距離より大きいなら次の距離を取り出す
    if cost > distance[current_node]:
        continue

    for v in G[current_node]:
        if Denger[v] == 2: continue
        
        if Denger[v] == 0:
            if cost + P < distance[v]:
                distance[v] = cost + P #最小コスト更新
                #heapに追加
                heapq.heappush(hQ, (distance[v], v))
        if Denger[v] == 1:
            if cost + Q < distance[v]:
                distance[v] = cost + Q #最小コスト更新
                #heapに追加
                heapq.heappush(hQ, (distance[v], v))

if Denger[N] == 0:
    print(distance[N]-P)
else:
    print(distance[N]-Q)