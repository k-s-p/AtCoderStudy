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
Q = deque()
Q.append(0)
depth = [0] * (N+1)
while len(Q) != 0:
    pos = Q.popleft()
    if depth[pos] == S+1:
        break
    
    for i in G[pos]:
        if depth[i] == 0:
            Q.append(i)
            depth[i] = depth[pos] + 1
            if Denger[i] == 0:
                Denger[i] = 1

print(Denger)