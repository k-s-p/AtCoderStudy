#幅優先探索で最短経路を出したのち、最短経路以外の道の白を黒にかえたらそれが答え

from collections import deque

dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下

def main():
    H,W = map(int, input().split())

    white = 0

    #探索のため外側を囲う
    G = [['#'] * (W+2) for _ in range(H+2)]
    for i in range(H):
        i_str = list(input())
        for j in range(W):
            G[i+1][j+1] = i_str[j]
            if i_str[j] == '.':
                white += 1
    
    #BFS
    Q = deque()
    Q.append((1,1))
    G[1][1] = 0
    ok = False #ゴールについたかどうか
    while len(Q) != 0:
        y,x = Q.popleft()
        if y == H and x == W:
            ok = True
            break

        for ii in range(4):
            ny = y+dy[ii]
            nx = x+dx[ii]
            if G[ny][nx] == '.':
                Q.append((ny, nx))
                G[ny][nx] = G[y][x] + 1

    if ok:
        print(white - 1 - G[H][W])
    else:
        print('-1')

if __name__ == '__main__':
    main()