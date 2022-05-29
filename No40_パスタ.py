#初の3次元DP
#dp[n][i][j]、iを一日前に食べ、jを二日前に食べてるn日目までのパターン数

MOD = 10**4
N,K = map(int, input().split())
A = [0] * N
for k in range(K):
    a, b = map(int, input().split())
    A[a-1] = b

dp = [[[0]*4 for i in range(4)] for j in range(N+1)]
dp[0][0][0] = 1 #ダミーのパスタ0(一日前、二日前が存在しないため)

#DP
for n in range(N):
    for i in range(4): #1日前のパスタ
        for j in range(4): #二日前のパスタ
            for k in range(1,4): #今日選ぶパスタ
                if A[n] != 0 and A[n] != k: #パスタが指定された日付で、kが違うパスタならスキップ
                    continue
                if k != i or i != j: #三日連続ではない場合
                    dp[n+1][k][i] += dp[n][i][j]
                    dp[n+1][k][i] %= MOD

ans = 0
for i in range(4):
    for j in range(4):
        #最終日にすべてのパターンを足す
        ans += dp[-1][i][j]
        ans %= MOD

print(ans)