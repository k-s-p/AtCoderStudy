from collections import deque

def main():
    dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
    dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下

    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    #地図
    G = [list(input()) for _ in range(R)]

    Q = deque()
    Q.append((sy-1,sx-1))
    G[sy-1][sx-1] = 0
    while len(Q) != 0:
        y,x = Q.popleft()

        for ii in range(4):
            ny = y+dy[ii]
            nx = x+dx[ii]
            if G[ny][nx] == '.':
                Q.append((ny, nx))
                G[ny][nx] = G[y][x] + 1
                
    print(G[gy-1][gx-1])

if __name__ == '__main__':
    main()