#入力の地図の中で、島を見つけたらDFSする。
#再帰で実装する
import sys
sys.setrecursionlimit(500000)
global G

#DFS(再帰関数)
dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下
def dfs(pos):
    y,x = pos
    G[y][x] = 2
    #これで全方位の探索ができるのでは？
    for ii in range(len(dx)):
        ny = y+dy[ii]
        nx = x+dx[ii]
        if G[ny][nx] == 1:
            s = (ny, nx)
            dfs(s)

while True:
    w,h = map(int, input().split())
    if w + h == 0:
        break
    #探索しやすくするため、入力の外側を0で囲う
    G = [[0 for i in range(w+2)] for j in range(h+2)]
    for i in range(h):
        a = list(map(int, input().split()))
        for j in range(1, w+1):
            G[i+1][j] = a[j-1]

    #探索開始
    ilands = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if G[i][j] == 1:
                s = (i,j)
                dfs(s)
                ilands += 1

    print(ilands)
        