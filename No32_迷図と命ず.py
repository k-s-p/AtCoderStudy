#解き方的には、横の壁と縦の壁をそれぞれ配列に格納
#普通に幅優先探索をするが壁を確認する

from collections import deque

dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下

def print_d(H, W, depth):
    print('*' * W)
    for i in range(H):
        print(*depth[i])

def bfs(G, h, w, x_wall, y_wall):
    Q = deque()
    Q.append((0,0))
    G[0][0] = 0
    while len(Q) != 0:
        y,x = Q.popleft()

        #左の移動時は、x_wall[y][x-1],右に移動時はx_wall[y][x]
        if x-1 >= 0 and x_wall[y][x-1] != 1 and G[y][x-1] == -1:
            Q.append((y, x-1))
            G[y][x-1] = G[y][x] + 1
        if x+1 < w and x_wall[y][x] != 1 and G[y][x+1] == -1:
            Q.append((y, x+1))
            G[y][x+1] = G[y][x] + 1
        #上の移動時は、y_wall[y-1][x],下の移動時はy_wall[y][x]
        if y-1 >= 0 and y_wall[y-1][x] != 1 and G[y-1][x] == -1:
            Q.append((y-1, x))
            G[y-1][x] = G[y][x] + 1
        if y+1 < h and y_wall[y][x] != 1 and G[y+1][x] == -1:
            Q.append((y+1, x))
            G[y+1][x] = G[y][x] + 1
    
    print(G[h-1][w-1] + 1) #出口は＋１する
    # print_d(h,w,G)

def main():
    while True:
        w,h = map(int, input().split())
        if w + h == 0:
            break
        x_wall = []
        y_wall = []

        for i in range(2*h - 1):
            wa = list(map(int, input().split()))
            if i % 2 == 0:
                x_wall.append(wa)
            else:
                y_wall.append(wa)
        
        G = [[-1] * w for i in range(h)]

        bfs(G, h, w, x_wall, y_wall)

if __name__ == '__main__':
    main()