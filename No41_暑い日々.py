D, N = map(int, input().split())
T = [int(input()) for i in range(D)]
C = [list(map(int, input().split())) for i in range(N)]

#n日目に服iを着た場合のスコアをdp[n][i]としてdpしたら解けるん？
dp = [[-10**8]*N for _ in range(D+1)] # 最大値を求める問題で、初日のスコアが0になるので-infで初期化

for n in range(D):
    t = T[n] #n日目の気温
    for i in range(N):
        if C[i][0] <= t <= C[i][1]:
            if n == 0:
                #初日はスコアが加算されない
                dp[n+1][i] = 0
                continue
            for j in range(N):
                #服jを選んだときの最大のスコアを保存
                dp[n+1][i] = max(dp[n][j] + abs(C[i][2]-C[j][2]), dp[n+1][i])
print(max(dp[-1]))