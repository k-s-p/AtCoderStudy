# ダイクストラ法で解ける
import heapq

V,E,r = map(int, input().split())
G = [[] for _ in range(V)]

# #辺が0なら終了
# if E == 0:
#     print(0)
#     exit()

# 有向隣接リストを作成
for i in range(E):
    s,t,d = map(int, input().split())
    G[s].append((t,d)) #sからtへ進むときの重みd
# print(G)
Q = []
INF = 10**10
#最短距離を格納
distance = [INF] * V
distance[r] = 0
#始点,開始の距離は0
heapq.heappush(Q, (0, r))
#ダイクストラ法で探索
while len(Q) != 0:
    (cost, current_node) = heapq.heappop(Q)
    
    #もし取り出した距離が記録されている最短距離より大きいなら次の距離を取り出す
    if cost > distance[current_node]:
        continue
    
    for v in G[current_node]:
        if distance[current_node] + v[1] < distance[v[0]]: 
            distance[v[0]] = distance[current_node] + v[1] #最短距離更新
            #heapに追加
            heapq.heappush(Q, (v[1], v[0]))

for i in distance:
    if i == INF:
        print('INF')
    else:
        print(i)