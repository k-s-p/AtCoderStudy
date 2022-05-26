#再帰DFSで解く
#渡れる薄氷の最大数は、その探索の深さとなる

import copy
import sys
sys.setrecursionlimit(int(1E+7))

global cnt

#DFS(再帰関数)
dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下
def dfs(Map, y, x, depth):
    Map[y][x] = 0
    global cnt
    cnt = max(cnt, depth)
    #これで全方位の探索ができるのでは？
    for ii in range(4):
        ny = y+dy[ii]
        nx = x+dx[ii]
        if Map[ny][nx] == 1:
            dfs(Map, ny, nx, depth+1)
    #割った氷を戻す
    Map[y][x] = 1

def main():
    M = int(input())
    N = int(input())

    #探索しやすくするため、入力の外側を0で囲う
    G = [[0 for i in range(M+2)] for j in range(N+2)]
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(1, M+1):
            G[i+1][j] = a[j-1]
            
    #区画を左上から総なめして、各薄氷ごとにDFSする
    ans = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                # G_copy = copy.deepcopy(G)
                global cnt
                cnt = 1
                dfs(G, i, j, cnt)
                ans = max(cnt, ans)
                
    print(ans)
    
if __name__ == "__main__":
    main()