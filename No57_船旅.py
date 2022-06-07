# ダイクストラ法で解ける
import heapq

INF = 10**10

n, k = map(int, input().split())
G = [[] for _ in range(n+1)]

def dks(n, start, goal):
    Q = []
    distance = [INF] * (n+1)
    #始点
    distance[start] = 0
    heapq.heappush(Q, (0, start))
    
    #探索
    while len(Q) != 0:
        (cost, current_node) = heapq.heappop(Q)
        
        if cost > distance[current_node]:
            continue
        
        for v in G[current_node]:
            if distance[current_node] + v[1] < distance[v[0]]: 
                distance[v[0]] = distance[current_node] + v[1] #最短距離更新
                #heapに追加
                heapq.heappush(Q, (v[1], v[0]))
    if distance[goal] == INF: return -1
    else: return distance[goal]

for i in range(k):
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        print(dks(n, inputs[1], inputs[2]))
    else:
        G[inputs[1]].append((inputs[2], inputs[3]))
        G[inputs[2]].append((inputs[1], inputs[3]))
