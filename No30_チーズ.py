from collections import deque

dy = [-1,1,0,0,-1,1,-1,1] #上下左右左上左下右上右下
dx = [0,0,-1,1,-1,-1,1,1] #上下左右左上左下右上右下

def main():
    H,W,N = map(int, input().split())
    sy, sx = -1,-1
    gy, gx = -1,-1
    #地図作成：探索しやすくするために外側を障害物で囲う
    G = [['X'] * (W+2) for j in range(H+2)]
    for i in range(H):
        input_str = list(input())
        for j in range(W):
            if input_str[j] == 'S': #巣の位置
                sy = i+1
                sx = j+1
            if input_str[j] == str(N): #巣の位置
                gy = i
                gx = j
            G[i+1][j+1] = input_str[j]
    
    #巣から探索を始めるが、チーズは1から順に食べることができる
    #DFSをチーズが見つかるまで行い、チーズがあれば、もう一度
    Q = deque()
    y, x = sy, sx
    d = 0
    for mouse in range(1,N+1):
        #深さを保持
        depth = [[-1] * W for _ in range(H)]
        depth[y-1][x-1] = d

        Q.append((y, x))

        while len(Q) != 0:
            y,x = Q.popleft()
            # print_d(H, W, depth)
            # print(y,x,mouse)
            if G[y][x] == str(mouse):
                d = depth[y-1][x-1]
                Q.clear()
                break

            #print(y,x)
            for ii in range(4):
                ny = y+dy[ii]
                nx = x+dx[ii]
                if G[ny][nx] != 'X' and depth[ny-1][nx-1] == -1:
                    # print(ny,nx)
                    Q.append((ny, nx))
                    depth[ny-1][nx-1] = depth[y-1][x-1] + 1

        # print(depth)
    print(depth[gy][gx])
    # print(depth)
    # print(G)

# def print_d(H, W, depth):
#     print('*' * W)
#     for i in range(H):
#         print(*depth[i])

if __name__ == '__main__':
    main()