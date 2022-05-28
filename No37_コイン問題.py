#DPの典型問題

n,m = map(int, input().split())
C = list(map(int, input().split()))

#横に金額で、コインの枚数を最小にするようにテーブルに書き込む
#一行のテーブルでいける
dp = [10 ** 18] * (n+1)
dp[0] = 0

for i in range(m):
    for j in range(C[i], n+1):
        dp[j] = min(dp[j], dp[j - C[i]] + 1)

print(dp[n])