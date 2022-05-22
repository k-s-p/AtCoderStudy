#順列全探索
#町を訪れる経路は順列nPnで表せるってこと?
import itertools
import math

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

cout = 0
sum_r = 0.0
for group in itertools.permutations(range(N)):
    cout += 1
    for i in range(1,N):
        dx = G[group[i-1]][0]-G[group[i]][0]
        dy = G[group[i-1]][1]-G[group[i]][1]
        sum_r += math.sqrt(dx*dx + dy*dy)

print(sum_r/cout)