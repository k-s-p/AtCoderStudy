N,M = map(int, input().split())
D = [int(input()) for i in range(N)]
C = [int(input()) for i in range(M)]

#joi君がj日かけて都市iに移動する最小の疲労度を求めていく
dp = [[10 ** 18] * (M+1) for i in range(N+1)]

#初日は疲労度0
for i in range(M+1):
    dp[0][i] = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        a = dp[i-1][j-1] + D[i-1]*C[j-1] #都市i-1から都市iへj日目に移動したときの疲労
        b = dp[i][j-1] #移動せずにとどまる
        dp[i][j] = min(a,b)
# print(dp)
print(dp[N][M]) #都市NにM日かけて到達したときの最小値となる