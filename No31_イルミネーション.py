#考え方的には、建物じゃないところを幅優先探索
#建物があれば、その壁をカウント
#yが偶数:左上、上、左、右、左下、下の方向が接してる六角形
#ｙが奇数：上、下、左、右、右上、右下の方向が接している六角形

from collections import deque

dy_e = [-1,1,0,0,-1,1] #上下左右左上左下
dx_e = [0,0,-1,1,-1,-1] #上下左右左上左下
dy_o = [-1,1,0,0,-1,1] #上下左右右上右下
dx_o = [0,0,-1,1,1,1] #上下左右右上右下

# def print_d(H, W, depth):
#     print('*' * W)
#     for i in range(H):
#         print(*depth[i])

def main():
    W, H = map(int, input().split())
    #探索のために地図の外側を囲う
    G = [[0] * (W+2) for j in range(H+2)]
    for i in range(H):
        input_str = list(map(int, input().split()))
        for j in range(W):
            G[i+1][j+1] = input_str[j]
    
    # print_d(H+2,W+2,G)
    Q = deque()
    ans = 0
    Q.append((0,0))
    G[0][0] = 2
    while len(Q) != 0:
        y,x = Q.popleft()
        if y % 2 == 0:
            for ii in range(6):
                ny = y+dy_e[ii]
                nx = x+dx_e[ii]
                if ny >= 0 and ny < H+2 and nx >= 0 and nx < W+2 and G[ny][nx] == 0:
                    Q.append((ny, nx))
                    G[ny][nx] = 2
                if ny >= 0 and ny < H+2 and nx >= 0 and nx < W+2 and G[ny][nx] == 1:
                    ans += 1
        else:
            for ii in range(6):
                ny = y+dy_o[ii]
                nx = x+dx_o[ii]
                if ny >= 0 and ny < H+2 and nx >= 0 and nx < W+2 and G[ny][nx] == 0:
                    Q.append((ny, nx))
                    G[ny][nx] = 2
                if ny >= 0 and ny < H+2 and nx >= 0 and nx < W+2 and G[ny][nx] == 1:
                    ans += 1
    print(ans)
    # print_d(H+2,W+2,G)

if __name__ == '__main__':
    main()