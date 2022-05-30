# 左の列から順に評価する
# n列目の色がcであるとき、塗り替えの最小値をdp[n][c]として記録する
N = int(input())
S = []
col = {'R':0, 'B':1, 'W':2, '#':-1}
for i in range(5):
    s = input()
    ls = list(s)
    ls = [-1] + [col[e] for e in ls] # 最も左の列にダミーを入れて置く
    S.append(ls)
dp = [[0]*3 for _ in range(N+1)]



for n in range(N):
    for i in range(3):
        cnt = 0
        for j in range(5):
            cnt += (S[j][n+1] != i)
        K = [0,1,2]
        K.remove(i) # 同じ色は隣合えない
        dp[n+1][i] = min(dp[n][K[0]] + cnt, dp[n][K[1]] + cnt)
print (min(dp[-1]))