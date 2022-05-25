global G
global t_1
global t_2
global t
global visited

def dfs(pos):
    global t
    visited[pos] = True
    t_1[pos] = t
    t += 1
    for i in G[pos]:
        if i == 0:
            continue
        if visited[i] == False:
            dfs(i)
    t_2[pos] = t
    t += 1

N = int(input())
G = [[]]
for i in range(N):
    g = list(map(int, input().split()))
    G.append(g[2:])

visited = [False] * (N+1)

#深さ優先探索
t = 1
t_1 = [0] * (N+1)
t_2 = [0] * (N+1)
for i in range(1,N+1):
    if visited[i] == True:
        continue
    else:
        dfs(i)

for i in range(1,N+1):
    print(i, t_1[i], t_2[i])